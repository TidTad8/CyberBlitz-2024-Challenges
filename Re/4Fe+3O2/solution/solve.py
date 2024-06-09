from pwn import *


def fib(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


p = remote("localhost", 30001)

# Level 1
p.sendlineafter(
    b"======== Level One ========",
    b"Rust is an iron oxide, a usually reddish-brown oxide formed by the reaction of iron and oxygen in the catalytic presence of water or air moisture."
)

# Level 2
p.recvuntil(b"Here's your magic number: ")
magic_number = int(p.recvline())
fibo = str(fib(magic_number)).encode()
p.sendline(fibo)

# Level 3
enc = xor(b"tasty", b"Rust was created because the creator had to climb 21 floors.")
p.sendlineafter(b"======= Level Three =======", enc)

# Get flag
log.success(p.recvall().decode().strip())


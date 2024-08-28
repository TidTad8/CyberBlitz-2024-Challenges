from pwn import *

HOST = "localhost"
PORT = 30001


def fib(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


p = remote(HOST, PORT)

# Level 1
p.sendlineafter(
    b"======== Level One ========",
    b"Rust is an iron oxide, a usually reddish-brown oxide formed by the reaction of iron and oxygen in the catalytic presence of water or air moisture."
)
p.recvuntil(b"Here is your flag: ")
log.success(f"Flag 1: {p.recvline().decode().strip()}")

# Level 2
p.recvuntil(b"Here's your magic number: ")
magic_number = int(p.recvline())
fibo = str(fib(magic_number)).encode()
p.sendline(fibo)
p.recvuntil(b"Here is your flag: ")
log.success(f"Flag 2: {p.recvline().decode().strip()}")

# Level 3
enc = xor(b"tasty", b"Rust was created because the creator had to climb 21 floors.")
p.sendlineafter(b"======= Level Three =======", enc)
p.recvuntil(b"Here is your flag: ")
log.success(f"Flag 3: {p.recvline().decode().strip()}")

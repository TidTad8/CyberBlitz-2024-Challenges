from Cryptodome.Random import random
from Cryptodome.Util import number
from Cryptodome.PublicKey import RSA
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Choose primes p and q
p = number.getPrime(1024)
q1 = number.getPrime(1024)

# Compute RSA key 1
n = p * q1
phi = (p - 1) * (q1 - 1)
key1 = RSA.construct(rsa_components=(n, 65537))
with open("alice_pubkey.pem", "wb") as f:
    data = key1.export_key()
    f.write(data)

# Compute RSA key 2
q2 = number.getPrime(1024)
n = p * q2
phi = (p - 1) * (q2 - 1)
key2 = RSA.construct(rsa_components=(n, 65537))
with open("bob_pubkey.pem", "wb") as f:
    data = key2.export_key()
    f.write(data)

# Read Alice's public key
with open("alice_pubkey.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(
        f.read()
    )

# Use Alice's public key to encrypt the flag (uses OAEP padding with MGF1 algorithm and SHA256)
flag = b"CyberBlitz{c0mM0N_fac7oR_i5_a_pr0b1eM}"
ciphertext = public_key.encrypt(
    flag,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
with open("ciphertext.enc", "wb") as f:
    f.write(ciphertext)
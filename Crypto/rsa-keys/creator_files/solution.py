from Cryptodome.PublicKey import RSA
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import math

# Read Alice's public key
with open("alice_pubkey.pem", "rb") as f:
    key = serialization.load_pem_public_key(
        f.read()
    )
alice_pubkey = key.public_numbers()

# Read Bob's public key
with open("bob_pubkey.pem", "rb") as f:
    key = serialization.load_pem_public_key(
        f.read()
    )
bob_pubkey = key.public_numbers()

# Compute the gcd of the two public moduli
p = math.gcd(alice_pubkey.n, bob_pubkey.n)

# If p != 1, we found one of the prime factors and can solve for private key d
if p != 1:
    q = alice_pubkey.n//p
    phi = (p - 1) * (q - 1)
    d = pow(alice_pubkey.e, -1, phi)
else:
    print("No vulnerability found!")

# Construct Alice's private key for decryption
key = RSA.construct(rsa_components=(alice_pubkey.n, alice_pubkey.e, d))
data = key.export_key()
private_key = serialization.load_pem_private_key(data, password=None)

# Use Alice's private key to decrypt ciphertext
with open("ciphertext.enc", "rb") as f:
    ciphertext = f.read()
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(plaintext)

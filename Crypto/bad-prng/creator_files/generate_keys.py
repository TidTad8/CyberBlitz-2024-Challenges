from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# Generate key
private_key = ec.generate_private_key(ec.SECP256R1)

# Write private key to PEM file (no encryption)
pem_private = private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.PKCS8,
   encryption_algorithm=serialization.NoEncryption()
)
with open("private.pem", "wb") as f: 
    f.write(pem_private)

# Convert EC private key to bytes
key = private_key.private_numbers().private_value
key = key.to_bytes(32, "big")

# Encrypt the flag with the key using AES CBC
flag = b"CyberBlitz{PrnG_i5_B4DlY_br0keN}"
iv = os.urandom(16)
padder = padding.PKCS7(128).padder()
padded_data = padder.update(flag) + padder.finalize()
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
ct = encryptor.update(padded_data) + encryptor.finalize()
ciphertext = iv + ct

# Write IV + Ciphertext into file
with open("ciphertext.enc", "wb") as f: 
    f.write(ciphertext)
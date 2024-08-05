from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os

def encrypt_data(data, key):
    key = key[:16]  # Ensure key is 16 bytes long
    iv = os.urandom(16)  # Generate a random IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    print("data: ", data)
    # Pad data to be a multiple of block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    print(f"Padded data: {padded_data.hex()}")
    encrypted_data = iv + encryptor.update(padded_data) + encryptor.finalize()
    print(f"Encrypted data: {encrypted_data.hex()}")
    return encrypted_data

def compute_shared_key(private_key, peer_public_key):
    shared_key = private_key.exchange(peer_public_key)
    return shared_key

# Load existing keys and parameters
def load_key(filename, private=True):
    with open(filename, 'rb') as f:
        if private:
            return serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )
        else:
            return serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )

# Example flag
flag = b'CyberBlitz{DH_n_M4n_1n_Th3_M1ddl3}'

# Load keys
alice_private_key = load_key('alice_private.pem')
bob_private_key = load_key('bob_private.pem')
evil_public_key = load_key('evil_public.pem', private=False)
intercepted_alice_pubkey = load_key('alice_public.pem', private=False)
intercepted_bob_pubkey = load_key('bob_public.pem', private=False)

# Compute shared keys
K1 = compute_shared_key(alice_private_key, evil_public_key)
K2 = compute_shared_key(bob_private_key, evil_public_key)

# Encrypt the flag into two parts
part1 = encrypt_data(flag[:len(flag)//2], K1)
part2 = encrypt_data(flag[len(flag)//2:], K2)

# Save the encrypted parts to files
def save_encrypted_data(filename, encrypted_data):
    with open(filename, 'wb') as f:
        f.write(encrypted_data)

save_encrypted_data('part1.enc', part1)
save_encrypted_data('part2.enc', part2)

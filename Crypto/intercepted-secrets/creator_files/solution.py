from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def decrypt_data(encrypted_data, key):
    key = key[:16]  # Ensure key is 16 bytes long
    iv = encrypted_data[:16]  # Extract the IV from the beginning
    encrypted_data = encrypted_data[16:]  # Extract the actual encrypted data
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    # Unpad data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

def compute_shared_key(private_key, peer_public_key):
    shared_key = private_key.exchange(peer_public_key)
    return shared_key

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

# Load keys
evil_private_key = load_key('evil_private.pem', private=True)
alice_public_key = load_key('alice_public.pem', private=False)
bob_public_key = load_key('bob_public.pem', private=False)

# Compute shared keys as Evil
K1 = compute_shared_key(evil_private_key, alice_public_key)
K2 = compute_shared_key(evil_private_key, bob_public_key)

# Load encrypted parts from files
def load_encrypted_data(filename):
    with open(filename, 'rb') as f:
        return f.read()

part1_enc = load_encrypted_data('part1.enc')
part2_enc = load_encrypted_data('part2.enc')

# Decrypt the parts using the shared keys
part1 = decrypt_data(part1_enc, K1)
part2 = decrypt_data(part2_enc, K2)

# Combine the parts to get the original flag
flag = part1 + part2
print(f"Decrypted flag: {flag.decode()}")

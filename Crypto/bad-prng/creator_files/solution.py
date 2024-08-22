from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# Read sig1
with open("sig1.der", "rb") as f:
    data = f.read()
    r1,s1 = utils.decode_dss_signature(data)

# Read sig2
with open("sig2.der", "rb") as f:
    data = f.read()
    r2,s2 = utils.decode_dss_signature(data)

# Hardcode secp256r1 curve parameters
# Order of group (prime q)
q = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551

# Compute hash values for the two messages
message = b"Message 1"
digest = hashes.Hash(hashes.SHA256())
digest.update(message)
h1 = digest.finalize()
h1 = int.from_bytes(h1, "big")
message = b"Message 2"
digest = hashes.Hash(hashes.SHA256())
digest.update(message)
h2 = digest.finalize()
h2 = int.from_bytes(h2, "big")

# Compute random value k used by the signer
k = ((h1 - h2) * pow(s1 - s2, -1, q)) % q

# Compute private key from s1
key = ((s1 * k - h1) * pow(r1, -1, q)) % q

# Convert EC private key to bytes
key = key.to_bytes(32, "big")

# Import ciphertext
with open("ciphertext.enc", "rb") as f:
    data = f.read()

# First 16 bytes is the IV, remaining is the ciphertext
iv = data[:16]
ct = data[16:]

# Decrypt ciphertext
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
decryptor = cipher.decryptor()
data = decryptor.update(ct) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
pt = unpadder.update(data) + unpadder.finalize()
print(pt)


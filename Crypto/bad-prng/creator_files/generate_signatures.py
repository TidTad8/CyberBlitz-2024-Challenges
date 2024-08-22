from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives import serialization
from Cryptodome.PublicKey import ECC
from Cryptodome.Random import random

# Read private key from file
with open("private.pem", "rt") as f:
    data = f.read()
    private = ECC.import_key(data, None)

# Hardcode secp256r1 curve parameters
# Order of group (prime q)
q = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
# Generator G (point)
g_x = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
g_y = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
G = ECC.EccPoint(g_x, g_y, curve='P-256')

# Generate first signature
k = random.randrange(q)
P = k * G
r = int(P.x % q)
message = b"Message 1"
digest = hashes.Hash(hashes.SHA256())
digest.update(message)
h = digest.finalize()
h = int.from_bytes(h, "big")
s = (h + r * int(private.d)) % q
inv_k = pow(k, -1, q)
s = (s * inv_k) % q
sig = utils.encode_dss_signature(r, s)
with open("sig1.der", "wb") as f: 
    f.write(sig)

# Generate second signature (with same k)
message = b"Message 2"
digest = hashes.Hash(hashes.SHA256())
digest.update(message)
h = digest.finalize()
h = int.from_bytes(h, "big")
s = (h + r * int(private.d)) % q
s = (s * inv_k) % q
sig = utils.encode_dss_signature(r, s)
with open("sig2.der", "wb") as f: 
    f.write(sig)
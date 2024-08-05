from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generate_parameters():
    # Generate parameters for Diffie-Hellman
    parameters = dh.generate_parameters(
        generator=2,
        key_size=2048,
        backend=default_backend()
    )
    return parameters

def generate_keypair(parameters):
    # Generate private key using parameters
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def save_key_to_file(key, filename, private=True):
    with open(filename, 'wb') as f:
        if private:
            f.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        else:
            f.write(key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

# Generate parameters and keys for Alice, Bob, and Evil
parameters = generate_parameters()

alice_private_key, alice_public_key = generate_keypair(parameters)
bob_private_key, bob_public_key = generate_keypair(parameters)
evil_private_key, evil_public_key = generate_keypair(parameters)

# Save keys to files
save_key_to_file(alice_private_key, 'alice_private.pem')
save_key_to_file(alice_public_key, 'alice_public.pem', private=False)
save_key_to_file(bob_private_key, 'bob_private.pem')
save_key_to_file(bob_public_key, 'bob_public.pem', private=False)
save_key_to_file(evil_private_key, 'evil_private.pem')
save_key_to_file(evil_public_key, 'evil_public.pem', private=False)

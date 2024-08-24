# Preparation
1. Run generate_keys.py
2. Provided files: Alice's and Bob's public keys, encrypted flag (with Alice's public key)

# Challenge Description
You have obtained two public keys from Alice and Bob. Although they look secure (2048-bit public modulus), you discovered a vulnerability that allowed you to recover both parties' private keys. You can retrieve the flag by decrypting the given ciphertext, which is encrypted under Alice's public key. Note that the RSA encryption involves a standard padding algorithm.

# Solution Thought Process
1. This is the common factor vulnerability that can break RSA security.
2. If two public moduli n1 and n2 contain a common factor, i.e., gcd(n1,n2) != 1, then both moduli are easily factored.
3. Find the common factor p, and get Alice's second factor q as q = n/p.
4. Having p and q, such that n = p*q, you can easily derive the private key d.
5. The RSA encryption involves OAEP padding with the MGF1 algorithm and SHA256 hashing.

# Flag
CyberBlitz{c0mM0N_fac7oR_i5_a_pr0b1eM}
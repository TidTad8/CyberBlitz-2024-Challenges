# Preparation
1. Run generate_keys.py
2. Run generate_signatures.py
3. Provided files: Two DER-encoded ECDSA signatures, encrypted flag

# Challenge Description
I have two DER-encoded ECDSA signatures generated by Alice's private key. The first signed message is "Message 1" and the second signed message is "Message 2". The signature algorithm uses the SECP256R1 curve with SHA-256 hashing. I noticed something weird on the two signatures, which allowed me to derive Alice's private key. That same key was also used to encrypt the flag with a symmetric cipher (AES in CBC mode). The IV is included at the start of the encrypted data.

# Solution Thought Process
1. The two signatures share the same r value, which indicates that they were produced with the same random value (a sign of a flawed PRNG implementation). 
2. Using the two formulas that produced the two signatures, solve for the two unknowns: the random value k and Alice's private key x.
3. x is also the AES key that encrypted the flag.
4. IV is known to be 16 bytes.
5. Use x and the IV to get the flag.

# Flag
CyberBlitz{PrnG_i5_B4DlY_br0keN}

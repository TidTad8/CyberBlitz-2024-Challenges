Creator: <a href="https://github.com/TidTad8">@TidTad8</a>

# Preperation
1. Run generate_keys.py
2. encrypt_flag.py
3. Provided files: alice & bob private keys, 2 part encrypted flag, attacker public & private keys

# Challenge Description
After I managed to intercept some communications between Alice and Bob since they were using DFKE, but shortly after I lost my decryption script.
I think the encryption being used is AES, the IV should be included at the start of the encrypted data.

# Solution Thought Process
1. Knowing its DFKE, the padding would be PKCS7. 
2. As for the AES mode, have to try each one, but the one being used if CFB.
3. IV is known to be 16 bytes.
4. Since the challenge context is a MITM attack, the shared keys between alice & evil, and bob & evil can be derived. 
5. The shared keys can then be used to decryot the 2 encrypted messages, 1 from each user, and combined to get the flag.

For more info:
https://medium.com/@lydia.cao26/diffie-hellman-key-exchange-basics-and-vulnerabilities-afc51342988e

# Flag
CyberBlitz{DH_n_M4n_1n_Th3_M1ddl3}
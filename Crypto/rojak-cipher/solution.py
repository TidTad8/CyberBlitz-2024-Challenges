import random

# Rail Fence Cipher Decryption
def rail_fence_decrypt(cipher, num_rails):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(num_rails)]
    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(num_rails):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1
    return "".join(result)

# XOR
def xor_decrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

# Caesar Cipher Decryption
def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Atbash Cipher Decryption
def atbash_cipher(text):
    def atbash_char(c):
        if 'A' <= c <= 'Z':
            return chr(ord('Z') - (ord(c) - ord('A')))
        elif 'a' <= c <= 'z':
            return chr(ord('z') - (ord(c) - ord('a')))
        else:
            return c
    return ''.join(atbash_char(c) for c in text)

# Keyword Cipher Decryption
def keyword_cipher_decrypt(text, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ""
    for char in keyword.upper():
        if char not in key:
            key += char
    for char in alphabet:
        if char not in key:
            key += char

    key_map = {key[i]: alphabet[i] for i in range(len(alphabet))}
    key_map.update({key[i].lower(): alphabet[i].lower() for i in range(len(alphabet))})

    plain_text = ""
    for char in text:
        if char.isalpha():
            plain_text += key_map[char]
        else:
            plain_text += char
    return plain_text


MY_FAVORITE_ROJAK = "PASEMBUR"
ROJAK_TYPES = 3
encrypted_keyword = "TbeK3B3j_eyoVjxt1hDnjeb_5Wf5}vg{t_e5_S"

# Step 1: Keyword Cipher
decrypted_keyword = keyword_cipher_decrypt(encrypted_keyword, MY_FAVORITE_ROJAK)
print(f"Decrypted Keyword Cipher: {decrypted_keyword}")

# Step 2: Atbash Cipher
decrypted_atbash = atbash_cipher(decrypted_keyword)
print(f"Decrypted Atbash Cipher: {decrypted_atbash}")

# Step 3: Julius Caesar Cipher (Shift by -3 to decrypt)
decrypted_caesar = caesar_cipher(decrypted_atbash, ROJAK_TYPES)
print(f"Decrypted Caesar Cipher: {decrypted_caesar}")

# Step 4: Rail Fence Cipher
decrypted_rail_fence = rail_fence_decrypt(decrypted_caesar, ROJAK_TYPES)
print(f"Final Decrypted Text: {decrypted_rail_fence}")

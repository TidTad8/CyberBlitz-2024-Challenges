# Rail Fence Cipher Encryption
# The rail fence cipher works by writing the plaintext in a zigzag pattern according to a given number of rails.
def rail_fence_encrypt(text, num_rails):
    rail = [['\n' for _ in range(len(text))] for _ in range(num_rails)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if row == 0 or row == num_rails - 1:
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        row += 1 if dir_down else -1

    result = []
    for i in range(num_rails):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

# XOR
def xor_encrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

# Caesar Cipher Encryption
# The Caesar cipher is a substitution cipher that shifts the alphabet by a certain number of characters.
def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Atbash Cipher Encryption
# atbash works by reversing the alphabet, so that the first letter becomes the last letter, the second letter becomes the second to last letter, and so on.
def atbash_cipher(text):
    def atbash_char(c):
        if 'A' <= c <= 'Z':
            return chr(ord('Z') - (ord(c) - ord('A')))
        elif 'a' <= c <= 'z':
            return chr(ord('z') - (ord(c) - ord('a')))
        else:
            return c
    return ''.join(atbash_char(c) for c in text)

# Keyword Cipher Encryption
# The keyword cipher is a substitution cipher that uses an alphabet that can be represented with a keyword.
def keyword_cipher(text, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ""
    for char in keyword.upper():
        if char not in key:
            key += char
    for char in alphabet:
        if char not in key:
            key += char

    key_map = {alphabet[i]: key[i] for i in range(len(alphabet))}
    key_map.update({alphabet[i].lower(): key[i].lower() for i in range(len(alphabet))})

    cipher_text = ""
    for char in text:
        if char.isalpha():
            cipher_text += key_map[char]
        else:
            cipher_text += char
    return cipher_text


# Encryption Process
MY_FAVORITE_ROJAK = "PASEMBUR"
ROJAK_TYPES = 3
FLAG = "CyberBlitz{cH1ck3N_fRitt3r5_i5_A_mU5t}"

# Step 1: Rail Fence Cipher
num_rails = ROJAK_TYPES
encrypted_rail_fence = rail_fence_encrypt(FLAG, num_rails)

# Step 2: Julius Caesar Cipher (Shift by 3)
encrypted_caesar = caesar_cipher(encrypted_rail_fence, ROJAK_TYPES)

# Step 3: Atbash Cipher
encrypted_atbash = atbash_cipher(encrypted_caesar)

# Step 4: Keyword Cipher
encrypted_keyword = keyword_cipher(encrypted_atbash, MY_FAVORITE_ROJAK)

print(f"Final Encrypted Text: {encrypted_keyword}")
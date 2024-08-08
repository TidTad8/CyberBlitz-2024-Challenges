
import base64
import base58

def rot13(word):
    result = []
    for letter in word:
        if 'a' <= letter <= 'z':
            result.append(chr((ord(letter) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= letter <= 'Z':
            result.append(chr((ord(letter) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(letter)
    return ''.join(result)

def base32_encoding(word):
    # encode string to bytes
    word_bytes = word.encode('utf-8')
    # apply base32 encoding
    encoded_bytes = base64.b32encode(word_bytes)
    # convert encoded bytes to string
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string


def base58_encoding(word):
    # encode string to bytes
    word_bytes = word.encode('utf-8')
    # apply base58 encoding
    encoded = base58.b58encode(word_bytes)
    return encoded.decode('utf-8')

# Example usage
Flag = "CyberBlitz{r0t_13_ANd_bA53s}"

cipher = rot13(Flag)
cipher = base58_encoding(cipher)
cipher = base32_encoding(cipher)
print(cipher)


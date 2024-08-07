# from PIL import Image
#
#
# def embed_text(image_path, text, output_path):
#     img = Image.open(image_path)
#     # Ensure image is in RGB mode
#     if img.mode != 'RGB':
#         img = img.convert('RGB')
#     binary_text = ''.join(format(ord(char), '08b') for char in text)
#
#     binary_index = 0
#     width, height = img.size
#     pixels = img.load()
#
#     for y in range(height):
#         for x in range(width):
#             if binary_index < len(binary_text):
#                 r, g, b = pixels[x, y]
#
#                 r = (r & ~1) | int(binary_text[binary_index])  # Embed one bit in R
#                 binary_index += 1
#                 if binary_index < len(binary_text):
#                     g = (g & ~1) | int(binary_text[binary_index])  # Embed one bit in G
#                     binary_index += 1
#                 if binary_index < len(binary_text):
#                     b = (b & ~1) | int(binary_text[binary_index])  # Embed one bit in B
#                     binary_index += 1
#
#                 pixels[x, y] = (r, g, b)  # Update pixel with new values
#             else:
#                 break
#
#     img.save('davinci_man_1.png')  # Save the modified image
#
#
# # Usage
# embed_text('davinci_man.png', 'CyberBlitz{R3al_3y35_R34l1z3_R34L_Li35}', 'davinci_man_1.png')
# print("embedded text")

from PIL import Image


def extract_text(image_path):
    img = Image.open(image_path)
    binary_text = ''

    width, height = img.size
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_text += str(r & 1)  # Extract least significant bit from R
            binary_text += str(g & 1)  # Extract least significant bit from G
            binary_text += str(b & 1)  # Extract least significant bit from B

    binary_chars = [binary_text[i:i + 8] for i in range(0, len(binary_text), 8)]  # Split into 8-bit chunks
    text = ''
    for binary_char in binary_chars:
        char = chr(int(binary_char, 2))  # Convert binary to character
        text += char
        if char == '}':
            break  # Stop at '}'

    return text  # Return the extracted text


# Usage
print("extracting LSB bits from RBG to form:  ")
hidden_text = extract_text('result.png')
print(hidden_text)

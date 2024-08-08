def convert_bits_to_dna(bit_sequence):
    # Mapping from bits to nucleotides
    mapping = {
        '00': 'A',
        '01': 'T',
        '10': 'C',
        '11': 'G'
    }

    # Split the bit sequence into chunks of 2 bits
    dna_sequence = ''.join(mapping[bit_sequence[i:i+2]] for i in range(0, len(bit_sequence), 2))

    return dna_sequence


# Input bit sequence
bit_sequence = "0100001101111001011000100110010101110010010000100110110001101001011101000111101001111011010000110111001001111001011100000111010001101111010111110110100101110011010111110111010001101000011001010101111101100110011101010111010001110101011100100110010101011111011100110111010101101001011010010110100101111101"
new_bit = bit_sequence.replace(" ", "")


# Convert bit sequence to DNA sequence
dna_sequence = convert_bits_to_dna(new_bit)

# Print the result
print(dna_sequence)

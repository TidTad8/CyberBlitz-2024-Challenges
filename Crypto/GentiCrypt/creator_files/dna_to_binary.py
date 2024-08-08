def convert_dna_to_bits(dna_sequence):
    # Mapping from nucleotides to bits
    mapping = {
        'A': '00',
        'T': '01',
        'C': '10',
        'G': '11'
    }

    # Convert each letter to its corresponding 2-bit representation
    bit_sequence = ''.join(mapping[nucleotide] for nucleotide in dna_sequence)

    return bit_sequence


# Input DNA sequence
dna_sequence = "TAAGTGCTTCACTCTTTGACTAACTCGATCCTTGTATGCCTGCGTAAGTGACTGCTTGAATGTATCGGTTGGTCCTTGAGTTGGTGTATCCATCTTTTGGTCTCTGTTTGTATGTTTGACTCTTTTGGTGAGTGTTTCCTTCCTTCCTTGGT"

# Remove spaces from the input sequence
dna_sequence = dna_sequence.replace(' ', '')

# Convert DNA sequence to bit sequence
bit_sequence = convert_dna_to_bits(dna_sequence)

# Print the result
print(bit_sequence)
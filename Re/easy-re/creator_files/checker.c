#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
void ascii_shift(char *str);
void unascii_shift(char *str);
void reverse_string(char *str);
void bitwise_xor(char *str, char key);
void unbitwise_xor(char *str, char key);
void bitwise_rotate(char *str, int n);
void unbitwise_rotate(char *str, int n);
void swap_characters(char *str);
void unswap_characters(char *str);
void hex_conversion(char *str, char *output);
void unhex(char *str, char *output);

int main() {
    char flag[] = "CyberBlitz{R3ally_3z_R3}";
    char temp_flag[256];

    // Step 1: ASCII shift
    strcpy(temp_flag, flag);
    ascii_shift(temp_flag);
    printf("After ascii_shift: %s\n", temp_flag);
    unascii_shift(temp_flag);
    printf("After unascii_shift: %s\n", temp_flag);

    // Step 2: Reverse the string
    strcpy(temp_flag, flag);
    reverse_string(temp_flag);
    printf("After reverse_string: %s\n", temp_flag);
    reverse_string(temp_flag); // Reversing again should restore original
    printf("After reverse_string (undo): %s\n", temp_flag);

    // Step 3: Bitwise XOR with a key
    strcpy(temp_flag, flag);
    bitwise_xor(temp_flag, 0x5A);
    printf("After bitwise_xor: %s\n", temp_flag);
    unbitwise_xor(temp_flag, 0x5A);
    printf("After unbitwise_xor: %s\n", temp_flag);

    // Step 4: Bitwise rotation
    strcpy(temp_flag, flag);
    bitwise_rotate(temp_flag, 3);
    printf("After bitwise_rotate: %s\n", temp_flag);
    unbitwise_rotate(temp_flag, 3);
    printf("After unbitwise_rotate: %s\n", temp_flag);

    // Step 5: Swap characters in pairs
    strcpy(temp_flag, flag);
    swap_characters(temp_flag);
    printf("After swap_characters: %s\n", temp_flag);
    unswap_characters(temp_flag);
    printf("After unswap_characters: %s\n", temp_flag);

    // Step 6: Hexadecimal conversion
    strcpy(temp_flag, flag);
    char hex_output[512];
    hex_conversion(temp_flag, hex_output);
    printf("After hex_conversion: %s\n", hex_output);
    unhex(hex_output, temp_flag);
    printf("After unhex: %s\n", temp_flag);

    return 0;
}

// Function implementations
void ascii_shift(char *str) {
    for (int i = 0; i < strlen(str); i++) {
        str[i] = str[i] + 1;
    }
}

void unascii_shift(char *str) {
    for (int i = 0; i < strlen(str); i++) {
        str[i] = str[i] - 1;
    }
}

void reverse_string(char *str) {
    int start = 0;
    int end = strlen(str) - 1;
    while (start < end) {
        char temp = str[start];
        str[start] = str[end];
        str[end] = temp;
        start++;
        end--;
    }
}

void bitwise_xor(char *str, char key) {
    for (int i = 0; i < strlen(str); i++) {
        str[i] = str[i] ^ key;
    }
}

void unbitwise_xor(char *str, char key) {
    for (int i = 0; i < strlen(str); i++) {
        str[i] = str[i] ^ key;
    }
}

void bitwise_rotate(char *str, int n) {
    for (int i = 0; i < strlen(str); i++) {
        unsigned char c = str[i];
        str[i] = (c << n) | (c >> (8 - n));
    }
}

void unbitwise_rotate(char *str, int n) {
    for (int i = 0; i < strlen(str); i++) {
        unsigned char c = str[i];
        str[i] = (c >> n) | (c << (8 - n));
    }
}

void swap_characters(char *str) {
    for (int i = 0; i < strlen(str) - 1; i += 2) {
        char temp = str[i];
        str[i] = str[i + 1];
        str[i + 1] = temp;
    }
}

void unswap_characters(char *str) {
    for (int i = 0; i < strlen(str) - 1; i += 2) {
        char temp = str[i];
        str[i] = str[i + 1];
        str[i + 1] = temp;
    }
}

void hex_conversion(char *str, char *output) {
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        sprintf(output + (i * 2), "%02x", (unsigned char)str[i]);
    }
    output[len * 2] = '\0';
}

void unhex(char *str, char *output) {
    char hex[3];
    hex[2] = '\0';
    int j = 0;
    for (int i = 0; i < strlen(str); i += 2) {
        hex[0] = str[i];
        hex[1] = str[i + 1];
        output[j] = (char)strtol(hex, NULL, 16);
        j++;
    }
    output[j] = '\0'; // Null-terminate the output string
}

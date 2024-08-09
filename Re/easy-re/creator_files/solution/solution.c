#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
void unhex(char *str, char *output);
void unswap_characters(char *str);
void unbitwise_rotate(char *str, int n);
void unbitwise_xor(char *str, char key);
void unreverse_string(char *str);
void unascii_shift(char *str);

int main() {
    char obfuscated_flag[] = "7321d148730901d1b9b973c131487909b98149c8c9e1f001"; // Replace with the obfuscated flag output
    char dehexed_flag[strlen(obfuscated_flag) / 2 + 1];

    // Step 1: Convert from hexadecimal
    unhex(obfuscated_flag, dehexed_flag);
    printf("After unhex: %s\n", dehexed_flag);

    // Step 2: Reverse the character swapping
    unswap_characters(dehexed_flag);
    printf("After unswap: %s\n", dehexed_flag);

    // Step 3: Reverse the bitwise rotation
    unbitwise_rotate(dehexed_flag, 3);
    printf("After unbitwise_rotate: %s\n", dehexed_flag);

    // Step 4: Reverse the XOR operation
    unbitwise_xor(dehexed_flag, 0x5A);
    printf("After unbitwise_xor: %s\n", dehexed_flag);

    // Step 5: Reverse the string reversal
    unreverse_string(dehexed_flag);
    printf("After unreverse_string: %s\n", dehexed_flag);

    // Step 6: Reverse the ASCII shift
    unascii_shift(dehexed_flag);
    printf("After unascii_shift: %s\n", dehexed_flag);

    // Final output
    printf("Deobfuscated flag: %s\n", dehexed_flag);

    return 0;
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

void unswap_characters(char *str) {
    for (int i = 0; i < strlen(str) - 1; i += 2) {
        char temp = str[i];
        str[i] = str[i + 1];
        str[i + 1] = temp;
    }
}

void unbitwise_rotate(char *str, int n) {
    for (int i = 0; i < strlen(str); i++) {
        unsigned char c = str[i];
        str[i] = (c >> n) | (c << (8 - n));
    }
}

void unbitwise_xor(char *str, char key) {
    for (int i = 0; i < strlen(str); i++) {
        str[i] = str[i] ^ key;
    }
}

void unreverse_string(char *str) {
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

void unascii_shift(char *str) {
    for (int i = 0; i < strlen(str); i++) {
        str[i] = str[i] - 1;
    }
}

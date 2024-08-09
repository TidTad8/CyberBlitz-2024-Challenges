#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
void ascii_shift(char *str);
void reverse_string(char *str);
void bitwise_xor(char *str, char key);
void bitwise_rotate(char *str, int n);
void swap_characters(char *str);
void insert_random_chars(char *str);
void hex_conversion(char *str);

int main() {
    char flag[] = "CyberBlitz{R3ally_3z_R3}";

    // Step 1: ASCII shift
    ascii_shift(flag);

    // Step 2: Reverse the string
    reverse_string(flag);

    // Step 3: Bitwise XOR with a key
    bitwise_xor(flag, 0x5A);

    // Step 4: Bitwise rotation
    bitwise_rotate(flag, 3);

    // Step 5: Swap characters in pairs
    swap_characters(flag);

    // Step 6: Hexadecimal conversion (optional for output)
    hex_conversion(flag);

    // Final output
    printf("Obfuscated flag: %s\n", flag);

    return 0;
}

void ascii_shift(char *str) {
    for (int i = 0; i < strlen(str); i++) {
        str[i] = str[i] + 1;
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

void bitwise_rotate(char *str, int n) {
    for (int i = 0; i < strlen(str); i++) {
        unsigned char c = str[i];
        str[i] = (c << n) | (c >> (8 - n));
    }
}

void swap_characters(char *str) {
    for (int i = 0; i < strlen(str) - 1; i += 2) {
        char temp = str[i];
        str[i] = str[i + 1];
        str[i + 1] = temp;
    }
}

void hex_conversion(char *str) {
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        printf("%02x", str[i]);
    }
    printf("\n");
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void a(char *z);
void b(char *z);
void c(char *z, char k);
void d(char *z, int n);
void e(char *z);
void f(char *z);

int main() {
    char g[] = "CyberBlitz{FAKE_FLAG}";

    a(g);
    b(g);
    c(g, 0x5A);
    d(g, 3);
    e(g);
    f(g);

    printf("Output: %s\n", g);

    return 0;
}

void a(char *z) {
    for (int i = 0; i < strlen(z); i++) {
        z[i] = z[i] + 1;
    }
}

void b(char *z) {
    int s = 0;
    int t = strlen(z) - 1;
    while (s < t) {
        char t = z[s];
        z[s] = z[t];
        z[t] = t;
        s++;
        t--;
    }
}

void c(char *z, char k) {
    for (int i = 0; i < strlen(z); i++) {
        z[i] = z[i] ^ k;
    }
}

void d(char *z, int n) {
    for (int i = 0; i < strlen(z); i++) {
        unsigned char c = z[i];
        z[i] = (c << n) | (c >> (8 - n));
    }
}

void e(char *z) {
    for (int i = 0; i < strlen(z) - 1; i += 2) {
        char t = z[i];
        z[i] = z[i + 1];
        z[i + 1] = t;
    }
}

void f(char *z) {
    int len = strlen(z);
    for (int i = 0; i < len; i++) {
        printf("%02x", z[i]);
    }
    printf("\n");
}

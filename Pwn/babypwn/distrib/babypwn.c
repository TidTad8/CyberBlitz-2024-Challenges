#include <stdio.h>
#include <stdlib.h>

void setupIO() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

void win() {
    system("/bin/sh");
}

void vuln() {
    char buffer[32];
    puts("Size of buffer: 32");
    printf("win() function: %p\n", win);
    printf("Your exploit string: ");
    gets(buffer);
    puts("Hope you got your shell!");
}

int main() {
    setupIO();
    vuln();
}

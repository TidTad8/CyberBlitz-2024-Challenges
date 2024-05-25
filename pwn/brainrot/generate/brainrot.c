#include <stdio.h>

char name[0x80];

void setupIO() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void vuln() {
    printf("Enter your skibidi rizz name: ");
    fgets(name, 0x80, stdin);
    printf("Wow that's some fanum taxing you got there ");
    printf(name);

    puts("Gimme a rizz description of yourself");
    char description[0x80];
    fgets(description, 0xa9, stdin);
}

int main() {
    setupIO();
    vuln();
    puts("Only true sigma rizzlers can gyatt in");
    return 0;
}

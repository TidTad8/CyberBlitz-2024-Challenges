# Challenge Preperation
gcc -o baby-re baby-re.c

# Challenge Description
NIL

# Solution
Decompile given binary file to get source code.

I used <a href="https://github.com/avast/retdec">Ret Decompiler</a> 

`./retdec-decompiler ~/Desktop/REEEE/baby-re`

Got C file among other files

Analyzing the methods in the given code, we can tell that the following functions are performed on the string:
1. ASCII shift
2. Reverse string characters
3. Bitwise XOR with a key
4. Bitwise rotation
5. Swap characters in pairs
6. Convert to Hexadecimal

To get the flag, implement code to reverse the above functions.

# Flag
CyberBlitz{R3ally_3z_R3}
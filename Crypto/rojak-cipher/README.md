Creator: <a href="https://github.com/TidTad8">@TidTad8</a>

# Challenge Description
I'm hiding the secret ingredient to my rojak recipe with my own cryptography algorithm, the ROJAK cipher.

It's simple, each letter represents a cipher which I mixed like rojak in order to get the best of each.

1. R - This ingredient was delivered by train.
2. O - I'm not using this ingredient.
3. J - I swapped out ingredient J for a classic Greek ingredient that will shift the flavor just right.
4. A - This ingredient comes from ancient traditions, mirroring the flavors perfectly.
5. K - This ingredient is like a family secret recipe, known only to those who possess the keyword.

I use my favorite rojak type as the keyword (all caps), and the number of rojak types for any numric keys.
https://travelerdoor.com/2020/08/10/the-different-types-of-rojak-you-can-find-in-malaysia/

# Solution
First, the ciphers used can be found with the challenge description and some research.

The ciphers used are: 
1. R - Railway cipher
2. J - Caesar cipher
3. A - Atbash cipher
4. K - Keyword cipher

We know that the railway & caesar ciphers use a number as the key, so we can assume the number of rojak types is the key for these ciphers.

The atbash cipher is a simple substitution cipher where the first letter of the alphabet is swapped with the last, the second with the second last, and so on.

The keyword cipher uses a keyword as the key, which should be the favorite rojak type "PASEMBUR".

Now we can decrypt the flag using the ciphers and keys we found.

Implement the decryption methods or use online tool like deCode to perform decryption in reverse order: K,A,J,R 

# Flag
CyberBlitz{cH1ck3N_fRitt3r5_i5_A_mU5t}
# solution for down-bad 05/26/2024
import gmpy2
import codecs
from Crypto.PublicKey import RSA
import base64
from itertools import *

with codecs.open('publickey.pem') as fr:
    pk = fr.read()
    pk = RSA.importKey(pk)

# file.enc
ct = "tD5ryHC86bGng+i9yy0lhsgHRYpbdFF5cNFue7lS+Z0Y9rA="
ct_decoded = base64.b64decode(ct)
print(ct_decoded)

#down-bad_key
with open('down-bad_key.enc', "r") as a:
    for line in a:
        key = line

print("exponent e: " + str(pk.e) + "\nvalue of n: " + str(pk.n))

# store them into mpz for accuracy
a1 = gmpy2.mpz(key)
a2 = gmpy2.mpz(pk.e)
a3 = gmpy2.mpz(pk.n)

# to find cubic root, use iroot
# need to test accordingly
y = a1 + a3
value, boolean = gmpy2.iroot(y, a2)
z = bytes.fromhex(hex(value)[2:])

# now XOR
xor_result = bytes(a ^ b for a, b in zip(ct_decoded, cycle(z)))
print(xor_result)
#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = ""
    shift_units = k % len(alphabet)  # modulus of full alphabet
    shift_alpha = alphabet[shift_units:] + alphabet[0:shift_units]  # shifted for Cipher construction
    for char in range(len(s)):  # Inserts all cipher charaters into one string
            
        if s[char].isalpha():
            letter_number = alphabet.find(s[char].lower())  # finds letter in original aphabet string
            if s[char].isupper():
                cipher_text += shift_alpha[letter_number].upper()
            else:
                cipher_text += shift_alpha[letter_number]
        else:
            cipher_text += s[char]  # checks for special characters
            
    return cipher_text
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    #     if i.capitalize() == full_string:
    #         continue
    #     if i.islower():
    #         full_string = full_string + " " + i.capitalize()
    #     elif i.isspace():
    #         full_string = full_string + " "
    #     else:
    #         full_string = full_string + " " + i
               # return "Here is your raw string: " + str(lowercase)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

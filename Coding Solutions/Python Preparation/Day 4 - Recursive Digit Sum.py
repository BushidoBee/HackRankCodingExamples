#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    first = get_sdsum(n)
    return check_line(str(int(first)*k))

def check_line(sd_str):
    if (len(sd_str) <= 1):
        return sd_str
    else:
        return check_line(get_sdsum(sd_str))

def get_sdsum(x):
    return str(sum((int(s) for s in list(x))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

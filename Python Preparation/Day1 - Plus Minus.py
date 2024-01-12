#!/bin/python3

import math
import os
import random
import re
import sys

# The function accepts INTEGER_ARRAY arr as parameter.

def plusMinus(arr):
    # IF STATEMENT | 1: arr[n] == 0; 3: arr[n] < 0; 3: arr[n] > 0
    less, more, zero = 0, 0, 0
    for number in arr:
        if number == 0: zero+=1
        elif number > 0: more+=1
        elif number < 0: less+=1
        else: continue
    print(more / len(arr), less / len(arr), zero / len(arr), sep='\n')

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)

#!/bin/python3

import math, os, random, re, sys

def lonelyinteger(a):
    for int_eval in a:
        if a.count(int_eval) >= 2: continue
        else: return a[a.index(int_eval)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    fptr.write(str(result) + '\n')
    fptr.close()

#!/bin/python3

import math, os, random, re, sys

def diagonalDifference(arr):
    matrix_size = int(len(arr))
    pri_diag, sec_diag, f_sec, s_sec = 0, 0, 0, 0
    for f_pri in range(matrix_size):
        pri_diag+=arr[f_pri][f_sec]
        f_sec+=1
    for s_pri in reversed(range(matrix_size)):
        sec_diag+=arr[s_pri][s_sec]
        s_sec+=1
    return abs(pri_diag - sec_diag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
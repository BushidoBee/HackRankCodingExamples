#!/bin/python3

import math, os, random, re, sys

def countingSort(arr):
    sort_alg = [0]*100
    for i in range(len(arr)):
        # sort_alg.append(arr.count(i))
        sort_alg[arr[i]]+=1
    return sort_alg

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
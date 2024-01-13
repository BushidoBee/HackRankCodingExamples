#!/bin/python3

import sys

def multiple(x):
    n1, n2, n3 = x//3, x//5, x//15
    return 3*(n1)*(n1+1)//2+5*(n2)*(n2+1)//2-15*(n3)*(n3+1)//2

steps = [3, 5]
for a0 in range(int(input())):
    n = int(input().strip())
    print(multiple(n-1))

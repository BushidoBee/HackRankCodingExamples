#!/bin/python3

import math
import os
import random
import re
import sys

def isBalanced(s):
    awaiting_pair = []
    bk_match = {'{': '}', '(': ')', '[': ']'}
    for n in range(len(s)):
        if s[n] in ['(', '{', '[']:
            awaiting_pair.append(s[n])
            # print(*bk_match.keys())
            
        else:
            if len(awaiting_pair) == 0:
                return 'NO'
            if bk_match.get(awaiting_pair.pop()) != s[n]:
                return 'NO'

    if len(awaiting_pair) > 0:
        return 'NO'

    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()
        print("Run #", t_itr+1)
        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

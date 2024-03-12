#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    for c_letter in range(len(grid[0])):
        for r_letter in range(1, len(grid)):
            if grid[r_letter][c_letter] < grid[r_letter-1][c_letter]:
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(sorted(grid_item))

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

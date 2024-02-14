#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    max_arr_sum = 0
    r_len = int(len(matrix))
    c_len = int(len(matrix))
    # Create the loop for full matrix
    for row in range(0, r_len // 2):
        for column in range(0, c_len // 2):
            lin_one, lin_two = row, r_len - row - 1  # Ensures rows are not out of bounds
            attr_one, attr_two = column, c_len - column - 1  # Ensures columns are not out of bounds
            
            # Grab maximum number in specified quadrant of matrix
            max_arr_sum = max_arr_sum + max(max(matrix[lin_one][attr_one], matrix[lin_one][attr_two]), max(matrix[lin_two][attr_one], matrix[lin_two][attr_two]))
    return max_arr_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()

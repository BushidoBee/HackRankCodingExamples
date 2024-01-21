#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
    # Remove minimum / maximum value from array
    eval_array = list(arr)
    
    # Print the result separated by " "
    print(sum(eval_array) - max(eval_array), sum(eval_array) - min(eval_array), sep=" ")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

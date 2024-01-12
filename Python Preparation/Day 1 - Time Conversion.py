#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    change_format = s.split(":")
    if change_format[2][-2:] == "AM" and change_format[0] == "12":
        return "00" + ":" + change_format[1] + ":" + change_format[2][:-2]
    elif change_format[2][-2:] == "AM":
        return str(change_format[0] + ":" + change_format[1] + ":" + change_format[2][:-2])
    elif change_format[2][-2:] == "PM" and change_format[0] == "12":
        return str(change_format[0] + ":" + change_format[1] + ":" + change_format[2][:-2])
    else:
        change_format[0] = str(int(change_format[0]) + 12)
        return str(change_format[0] + ":" + change_format[1] + ":" + change_format[2][0:2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()

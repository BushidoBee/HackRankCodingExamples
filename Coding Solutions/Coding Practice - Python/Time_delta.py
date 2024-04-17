#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta, timezone

# Complete the time_delta function below.
def time_format(timestamp):
    Month_Key = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    dt_split = timestamp[3:].strip().split()
    time_sp = dt_split[3].split(":")
    tz_sign = int(dt_split[-1][0] + "1")
    t_calc = tz_sign * int(dt_split[-1][1:3]) * 60 + tz_sign * int(dt_split[-1][3:5])
    
    t_delta = timedelta(minutes=t_calc)
    tz = timezone(t_delta)
    date = datetime(int(dt_split[2]), int(Month_Key[dt_split[1]]), int(dt_split[0]), int(time_sp[0]), int(time_sp[1]), int(time_sp[2]), tzinfo=tz)
    return (date)

def time_delta(t1, t2):
    dferece = time_format(t1) - time_format(t2)
    
    return (str(abs(int(dferece.total_seconds()))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

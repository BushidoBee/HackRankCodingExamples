import numpy

def arrays(arr):
    # complete this function
    blank = numpy.array(arr[::-1], float)
    # blank_sec = arr
    # use numpy.array
    return blank

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

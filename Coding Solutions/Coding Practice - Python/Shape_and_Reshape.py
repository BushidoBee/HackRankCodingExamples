import numpy

input_set = list(map(int, input().split()))
# print("Here's the input string: " + str(input_set))

my_array = numpy.reshape(input_set, (3, 3))
# print("Here's the Re-Shape Array: " + str(my_array))
print(my_array)

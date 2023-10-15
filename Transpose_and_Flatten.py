import numpy
input_one, input_two = map(int, input().split())

input_set = []

for create_array in range(input_one):
    tuple_var = list(map(int, input().split()))
    input_set.append(tuple_var)
array_set = numpy.array(input_set)
print(array_set.transpose())
print(array_set.flatten())

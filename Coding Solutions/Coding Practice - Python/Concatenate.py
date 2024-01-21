import numpy

n, m, p = map(int, input().split())
# print("Here's your objective: " + str(n) + " rows of 'N' | " + str(m) + " rows of 'M' | Columns: " + str(p))

full_array = []
np_input = []

for tuple_num in range(n+m):
    elem_1, elem_2 = map(int, input().split())
    np_input = [elem_1, elem_2]
    # print("Row #" + str(tuple_num+1) + ": (" + str(elem_1) + ", " + str(elem_2) +")")
    # print("Row #" + str(tuple_num+1) + ": " + str(np_input))
    full_array.append(np_input)

# print("Final result: ")
# print("Final result: " + str(full_array.reshape(n, m)))
print(str(numpy.reshape(full_array, (n+m, p))))

# Two sets: "M" and "N"; input size then coressponding contents
M_size, arr_M = input(), set(map(int, input().split(' ')))
N_size, arr_N = input(), set(map(int, input().split(' ')))

# Evaluate the symmetric differences of "M and "N"
# print(arr_M, arr_N)
sym_diff_one = sorted(list(arr_M.symmetric_difference(arr_N)))

# Print the result, separate on new line
print(*(sym_diff_one[i] for i in range(len(sym_diff_one))), sep='\n')

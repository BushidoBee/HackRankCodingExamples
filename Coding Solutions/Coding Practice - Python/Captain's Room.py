import collections

k = int(input())  # First input (Integer)

all_numbers = map(int, input().split())  # Second input (Integer | Array)

dictionary = collections.Counter(all_numbers)  # Collections dictionary of "all_numbers"

print(*[x for x, y in dictionary.items() if y != k])  # conditional list comprehension; unpack variable

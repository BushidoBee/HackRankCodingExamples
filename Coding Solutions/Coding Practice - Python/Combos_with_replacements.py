# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools # using itertools.combinations function library

# input 's', and 'num'; insert into variables
s , char_n = input().split()
num = int(char_n)
# use "Combinations" Function to create your replacement list; test to see result
r_combo = itertools.combinations_with_replacement(sorted(s), num)
for replacements in r_combo:
    print(''.join(replacements))

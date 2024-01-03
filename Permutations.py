### Permutations creates all combinations of list items / iterables
import itertools
# Define the Alphabet in a String variable 'Alpha'
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Create a permutation and set it to a variable; Extra check: If 'string' is all UPPERCASE
string, numchars = input().split()
num = int(numchars)
strperm = itertools.permutations(string, num)
print (list(strperm))
iteration = 0

# Print the permutations in alphabetical order using a loop; remove the selection from the list
for letter in ALPHA
    # Note: Slice the permutation to only 2 characters
    if letter in strperm[iteration]
    

### Permutations creates all combinations of list items / iterables
import itertools

# Create a permutation and set it to a variable; Extra check: If 'string' is all UPPERCASE
string, numchars = input().split()
num = int(numchars)
strperm = sorted(list(itertools.permutations(string, num))) # Note: Slicing the permutation to only 2 characters
print (strperm)

# Print the permutations in alphabetical order using a loop; remove the selection from the list
for iteration in range(len(strperm)):
    iterable = strperm[iteration][0] + strperm[iteration][1]
    print(iterable) # print the interation
        
    

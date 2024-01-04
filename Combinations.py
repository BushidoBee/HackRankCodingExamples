# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

# Create a Combination and set it to a variable
s , n  = input().split()
for i in range(1, int(n)+1):
    for j in itertools.combinations(sorted(s), i):
        print (''.join(j))

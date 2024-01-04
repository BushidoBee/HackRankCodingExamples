# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
import collections
# Will be using "groupby()" function and other associated with the "Itertools" library
# itertools.groupby(iterable[, key])
s = input()
string_one = itertools.groupby(s)
print (list(string_one[0]))


# Use a loop, iterate through all of the groups; end it with a space


# print the results


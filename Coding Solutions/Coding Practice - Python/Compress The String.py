# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
# Will be using "groupby()" function and other associated with the "Itertools" library
# itertools.groupby(iterable[, key])
s = input()
groups = []
string_one = list(itertools.groupby(s))
# print(list(string_one))


# Use a loop, iterate through all of the groups; end it with a space
for key, group_obj in itertools.groupby(s):
    groups.append("(" + str(len(list(group_obj))) + ", " + str(key) + ")")

# print the results
print(*groups)

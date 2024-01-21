# Enter your code here. Read input from STDIN. Print output to STDOUT
# Use collections.Counter() and itertools.combinations()
import collections, itertools

# Enter variables: Int(n), string(chars), int(k)
n = int(input())
chars = list(input().split())
k = int(input())
combinations = list(itertools.combinations(chars, k))
incr = 0

# Test your input results
# print(n, chars, k)
# let_combos = list(itertools.combinations(chars, k))
# print(list(chars))

# Loop through all possible tuples with indices of 'k'
for comb_set in combinations:
    # Increment 'incr' of matches if a character match is was found
    if 'a' in comb_set:
        # print("Letter #" + str(letter_num) + ": Match Found --> " + str(character) + " | " + str(let_combos[set_num]))
        incr+=1
    else:
        continue


# Divide 'incr' by the length of unordered tuples; Print the result
print("{:.4f}".format(incr / len(combinations))) # Floating format

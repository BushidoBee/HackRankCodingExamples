# Pypy 3 Version
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))


# Python 3 Version
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
print("Here is the number of elements: " + str(n))
hashtext = tuple(map(int, raw_input().split()))
concatenation = ""

# for combine in range(n):
#     print("Combining element #" + str(n) + ": " + str(hashtext[combine]))
#     concatenation = concatenation + str(hashtext[combine])

t = hash(tuple(hashtext))
print("Hash Value:")
print(hash(tuple(hashtext)))

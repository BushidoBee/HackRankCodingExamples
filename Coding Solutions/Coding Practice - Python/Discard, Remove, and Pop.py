n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    command = input().split()
    
    if command[0] == 'discard':
        # print("Loop ", i, " | option #1: ", command[0], " ", command[1])
        s.discard(int(command[1]))
        # print(s)
        
    elif command[0] == 'remove' and int(command[1]) in s:
        # print("Loop ", i, " | option #2: ", command[0], " ", command[1])
        s.remove(int(command[1]))
        # print(s)
        
    elif command[0] == 'pop':
        # print("Loop ", i, " | option #3: ", command[0])
        s.pop()
        # print(s)
        
    else:
        continue
        
print(sum(s))

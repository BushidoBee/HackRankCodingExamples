from collections import deque
dq = deque()

for i in range(int(input())):
    command = input().split()
    
    if command[0] == 'appendleft':
        dq.appendleft(int(command[1]))
        
    elif command[0] == 'append':
        dq.append(int(command[1]))
        
    elif command[0] == 'popleft':
        dq.popleft()
        
    elif command[0] == 'pop':
        dq.pop()
        
    else:
        continue
        
print(*dq)

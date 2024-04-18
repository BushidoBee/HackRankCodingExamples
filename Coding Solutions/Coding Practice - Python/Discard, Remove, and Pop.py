n = int(input())
s = set(map(int, input().split()))
ticks = int(input())
while (ticks > 0):
    ticks-=1
    action = input().split()
    
    if action[0] == 'pop' and :
        s.pop()
    if action[0] == 'remove' and action[1] in s:
        s.remove(int(action[1]))
    if action[0] == 'discard':
        s.discard(int(action[1]))
    else:
        break
        
print(sum(s))

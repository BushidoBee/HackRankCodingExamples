import collections
len_a, len_b = map(int, input().split())
letter = collections.defaultdict(list)
other_list = []
    
for i in range(len_a):
    letter[str(input())].append(i+1)
    
for i in range(len_b):
    other_list.append(str(input()))
    
for item in other_list:
    if item in letter.keys():
        print(*letter[item])
    else:
        print("-1")

A_Num = input()
Set_A = set(sorted([x for x in map(int, input().split())]))
cmd_valid = ["intersection_update", "symmetric_difference_update", "difference_update", "update"]
for cmd_num in range(int(input())):
    command = input().split()
    new_set = set(map(int, input().split()))
    
    eval('Set_A.{}({})'.format(command[0], new_set))


print(sum(Set_A))

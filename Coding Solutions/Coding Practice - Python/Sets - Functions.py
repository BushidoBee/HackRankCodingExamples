A_num, Set_A = input(), set(map(int, input().split()))
B_num, Set_B = input(), set(map(int, input().split()))

print(len(Set_A.union(Set_B)))
print(len(Set_A.intersection(Set_B)))
print(len(Set_A.difference(Set_B)))
print(len(Set_A.symmetric_difference(Set_B)))

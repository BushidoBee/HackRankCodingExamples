# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

Final_Prod = ""
ElemA = list(map(int, input().split()))
# print(ElemA)
ElemB = list(map(int, input().split()))
# print(ElemB)
Cart_Prod = list(itertools.product(ElemA, ElemB, repeat=1))
for loop in range(len(Cart_Prod)-1):
    Final_Prod = Final_Prod + str(Cart_Prod[loop]) + " "
Final_Prod = Final_Prod + str(Cart_Prod[loop+1])
print(Final_Prod)

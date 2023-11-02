# Enter your code here. Read input from STDIN. Print output to STDOUT
length, width = map(int, input().split())
half_length = length // 2
dash = "-"
design = ".|."
message = "WELCOME"
ptrn_cnt = 1

# print("Here are your dimensions: " + str(length) + " x " + str(width))

for halfdesign_1 in range(half_length):
    ins_pat = design * ptrn_cnt
    l_dashes = dash * ((width - len(ins_pat)) // 2)
    r_dashes = l_dashes
    print(l_dashes + ins_pat + r_dashes)
    ptrn_cnt += 2

mid_dash = dash * ((width - len(message)) // 2)
print(mid_dash + message + mid_dash)

for halfdesign_2 in range(half_length):
    ptrn_cnt -= 2
    ins_pat = design * ptrn_cnt
    l_dashes = dash * ((width - len(ins_pat)) // 2)
    r_dashes = l_dashes
    print(l_dashes + ins_pat + r_dashes)

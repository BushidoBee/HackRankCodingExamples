def findZigZagSequence(a, n):
    zz = a.copy()
    zz.sort()
    mid = int(n / 2)
    # print("The middle is:", mid)
    zz[mid], zz[n-1] = zz[n-1], zz[mid]
    # print("After Step 1:", zz)

    zz[mid+1:-1] = reversed(zz[mid+1:-1])
    # print("After Step 2:", zz)

    for i in range(n):
        if i == n-1:
            print(zz[i])
        else:
            print(zz[i], end = ' ')
    return

test_cases = int(input())
for cs in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)

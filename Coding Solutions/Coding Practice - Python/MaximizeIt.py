# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    k, mod_val = map(int, input().split())
    max_total = 0
    max_magnitude = pow(10, 9)
    magnitude_array = []

    for line_num in range(k):
        inner_array = []
        m = list(map(int, input().split()))
        # print("Line #" + str(line_num+1) + ": " + str(list(m[1::])))
        inner_array = m[1::]
        inner_array.sort(reverse=True)
        print("Evaluating List Line #" + str(line_num+1) + ": " + str(list(inner_array)))

        for subset_num in range(m[0]):
            max_num = int(inner_array[subset_num])
            # maximum_num = pow(max_num, 2)
            test_magnitude = sum(magnitude_array) + max_num
            # print("Testing Max Number: " + str(max_num))
            if test_magnitude < max_magnitude:
                print("Success: Now appending best maximum number: " + str(max_num))
                magnitude_array.append(max_num)
                break
            else:
                continue
    max_total = sum(magnitude_array)
    print("List Magnitudes: " + str(list(magnitude_array)))
    print("Magnitude Total: " + str(max_total))

    answer = pow(max_total, 2) % mod_val
    print("The Answer is: " + str(answer))
    # print(answer)

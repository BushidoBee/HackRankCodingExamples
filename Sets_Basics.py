def average(array):
    # Change the array into a set; calculate the average
    arr_set = set(array)
    # Output average --> Sum(Heights) / Heights Count
    average = float(sum(arr_set) / len(arr_set))
    return average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

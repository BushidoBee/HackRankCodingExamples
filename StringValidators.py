if __name__ == '__main__':
    s = list(input())
    # print("Here is the string, split-up: " + str(s))
    print(any(teststr.isalnum() for teststr in s))
    print(any(teststr.isalpha() for teststr in s))
    print(any(teststr.isdigit() for teststr in s))
    print(any(teststr.islower() for teststr in s))
    print(any(teststr.isupper() for teststr in s))

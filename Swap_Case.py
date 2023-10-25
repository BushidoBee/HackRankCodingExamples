def swap_case(s):
    case_swap = s.swapcase()
    return case_swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

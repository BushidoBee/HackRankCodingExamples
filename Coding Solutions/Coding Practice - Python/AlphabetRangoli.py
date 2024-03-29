def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    pattern_size = 2
    for i in reversed(range(size)):
        pattern = ""
        for a in alpha[i:size]:
            pattern = pattern + a + "-"

        full_pattern = pattern[::-1] + pattern[1:]
        # print("Line: " + full_pattern[1:pattern_size])
        field = "-" * (i*2)
        print(field + full_pattern[1:pattern_size] + field)
        pattern_size+=4

    pattern_size = pattern_size - 8

    for i in range(1, size):
        pattern = ""
        for a in alpha[i:size]:
            pattern = pattern + a + "-"

        full_pattern = pattern[::-1] + pattern[1:]
        field = "-" * (i*2)
        print(field + full_pattern[1:pattern_size] + field)
        pattern_size-=4

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

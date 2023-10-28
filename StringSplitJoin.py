def split_and_join(line):
    # write your code here
    list_line = line.split(" ")
    conjoined_line = "-".join(list_line)
    return conjoined_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

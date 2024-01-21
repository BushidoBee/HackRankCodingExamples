def count_substring(string, sub_string):
    match_found = 0
    stop_pos = int(len(sub_string))

    # print("Sub-String targeted: " + str(sub_string))

    for str_pos in range(0, len(string)):
        sliced_str = string[slice(str_pos, stop_pos)]
        # str_stop_pos = sub_str_len + str_pos
        # slice_str = string[str_pos:str_stop_pos]
        # str_slice = slice(str_pos, sub_str_len)
        # print("String Slice Value: '" + str(sliced_str) + "'")
        if sliced_str == sub_string:
            match_found+=1
        stop_pos+=1
    return match_found

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

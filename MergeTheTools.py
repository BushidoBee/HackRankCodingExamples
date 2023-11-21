def merge_the_tools(string, k):
    strp, endp = 0, k
    segments = len(string) // k
    for t in range(segments):
        # split = string[strp:endp]
        # print("Here is you string: " + str(split))
        
        augsplit = list(dict.fromkeys(string[strp:endp]))
        
        print("".join(augsplit))
        strp+=k
        endp+=k
    return 0

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

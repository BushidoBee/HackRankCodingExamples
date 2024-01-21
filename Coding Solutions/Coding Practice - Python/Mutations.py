def mutate_string(stri, pos, char):
    mutation = list(stri)
    mutation[pos] = char
    f_mutation = ''.join(mutation)
    return f_mutation

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

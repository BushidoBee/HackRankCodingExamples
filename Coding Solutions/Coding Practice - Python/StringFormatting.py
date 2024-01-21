def print_formatted(number):
    line_width = len(bin(number)[2:])
    for digit in range(1, number+1):
        integer = str(digit)
        octal = oct(digit)[2:]
        hexa = hex(digit)[2:].upper()
        binary = bin(digit)[2:]
        print(integer.rjust(line_width), octal.rjust(line_width), hexa.rjust(line_width), binary.rjust(line_width))
    return 0

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

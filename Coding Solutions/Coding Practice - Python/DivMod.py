x, y = int(input()), int(input())
div_mod, modulus, division = divmod(x, y), x % y, x//y
print(str(division), str(modulus), str(div_mod), sep='\n')

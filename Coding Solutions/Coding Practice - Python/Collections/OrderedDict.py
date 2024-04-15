from collections import OrderedDict
items = int(input())
cart = OrderedDict()
for _ in range(items):
    item = input().rsplit(maxsplit=1)
    if item[0] in cart:
        cart[item[0]] += int(item[1])
    else:
        cart[item[0]] = int(item[1])
for group, product in cart.items():
    print(group, product)

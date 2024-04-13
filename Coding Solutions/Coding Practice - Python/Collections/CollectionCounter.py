# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
# Input: Shoe Quantity, Sizes and Customer Count, initialize Grand total Array
ShoeQnty = int(input())
# Stock = list(input().split())
Stock = dict(Counter(input().split()))
Customers = int(input())
grand_total = 0


# print(str(ShoeQnty) + " | ", Stock, " | ", str(Customers))

# Iterate to add all of the Shoe sizes purchased and price; pop out sizes already purchased
for buyer in range(Customers):
    shoe_size, price = input().split()
    # print("Loop #", buyer+1, " | ", shoe_size, " / ", price)
    if shoe_size in Counter(Stock).keys() and Stock[shoe_size] > 0:
        grand_total = grand_total + int(price)
#       print("Adding price: ", price)
        Stock[shoe_size]-=1
#       print("Now ", Stock[shoe_size], " left.")

# Display the result
print(grand_total)

price_total = 0
RESTRICT = 100
DISCOUNT = 0.9
number = int(input("Number of items: "))
for i in range(number):
    price_each = float(input("Price of item: "))
    price_total = price_total + price_each
if price_total > RESTRICT:
    price_total = price_total * DISCOUNT
print(f"Total price for {number} items is ${price_total:.2f}")

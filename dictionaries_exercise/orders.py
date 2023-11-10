command = input()
products = {}

while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][0] = price
        products[name][1] += quantity
    command = input()

for product, info in products.items():
    print(f"{product} -> {(info[0] * info[1]):.2f}")

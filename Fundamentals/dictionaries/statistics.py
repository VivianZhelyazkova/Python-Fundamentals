products_in_stock = {}

command = input()

while command != "statistics":
    key, value = command.split(": ")
    if key in products_in_stock.keys():
        products_in_stock[key] += int(value)
    else:
        products_in_stock[key] = int(value)
    command = input()
print("Products in stock:")
for product,quantity in products_in_stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products_in_stock)}")
print(f"Total Quantity: {sum(products_in_stock.values())}")
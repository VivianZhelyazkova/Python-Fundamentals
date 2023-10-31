products = input().split()
searched_products = input().split()
products_in_stock = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    products_in_stock[key] = int(value)

for product in searched_products:
    if product in products_in_stock.keys():
        print(f"We have {products_in_stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
product = input()
quantity = int(input())


def total_price(name, number):
    if name == "coffee":
        price = 1.50
    elif name == "water":
        price = 1.00
    elif name == "coke":
        price = 1.40
    elif name == "snacks":
        price = 2.00
    result = price * number
    return result


print(f"{total_price(product,quantity):.2f}")
    
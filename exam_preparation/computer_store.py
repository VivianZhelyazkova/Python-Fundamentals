command = input()
total_price = 0

while command != "special" and command != "regular":
    price = float(command)
    if price > 0:
        total_price += price
    else:
        print("Invalid price!")
    command = input()

if total_price <= 0:
    print("Invalid order!")
else:
    tax = total_price * 0.2
    total_with_tax = total_price + tax

    if command == "special":
        total_with_tax = total_with_tax * 0.90

    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_with_tax:.2f}$")

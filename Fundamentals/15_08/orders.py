number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01\
            or price_per_capsule > 100.00\
            or 31 < days\
            or days < 1\
            or 2000 < capsules_per_day\
            or capsules_per_day < 1:
        continue
    coffe_price = days * capsules_per_day * price_per_capsule
    print(f"The price for the coffee is: ${coffe_price:.2f}")
    total_price += coffe_price
print(f"Total: ${total_price:.2f}")





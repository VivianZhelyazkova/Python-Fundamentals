train_ticket = 150
collection = input().split("|")
budget = float(input())
new_budget = 0
budget_left = budget
spend = 0

clothes_maximum = 50.00
shoes_maximum = 35.00
accessories_maximum = 20.50

list_of_new_prices = []

for item in collection:
    item_type, item_price = item.split('->')
    item_price = float(item_price)

    if item_type == "Clothes":
        if item_price <= clothes_maximum and budget_left >= item_price:
            budget_left -= item_price
            new_price = item_price * 1.40
            spend += item_price
            new_budget += new_price
            list_of_new_prices.append("{:.2f}".format(new_price))
    elif item_type == "Shoes":
        if item_price <= shoes_maximum and budget_left >= item_price:
            budget_left -= item_price
            new_price = item_price * 1.40
            spend += item_price
            new_budget += new_price
            list_of_new_prices.append("{:.2f}".format(new_price))
    elif item_type == "Accessories":
        if item_price <= accessories_maximum and budget_left >= item_price:
            budget_left -= item_price
            new_price = item_price * 1.40
            spend += item_price
            new_budget += new_price
            list_of_new_prices.append("{:.2f}".format(new_price))

profit = new_budget - spend
total_money = new_budget + budget_left

print(*list_of_new_prices, sep=" ")
print(f"Profit: {profit:.2f}")
if total_money >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")


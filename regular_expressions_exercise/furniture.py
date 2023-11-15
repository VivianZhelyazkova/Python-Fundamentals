import re

information = input()
regex = ">{2}([a-zA-Z]+)<{2}([0-9]+(?:.[0-9]*))!([0-9]+)"
valid_purchases = []
total_money = 0
while information != "Purchase":
    valid_purchase = re.findall(regex, information)
    if len(valid_purchase) == 0:
        information = input()
        continue
    information = input()
    total_money += float(valid_purchase[0][1]) * int(valid_purchase[0][2])
    valid_purchases.append(valid_purchase[0][0])

print(f"Bought furniture:")
for purchase in valid_purchases:
    print(purchase)
print(f"Total money spend: {total_money:.2f}")

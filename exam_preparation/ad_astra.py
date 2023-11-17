import re

products = input()

regex = r"([\|#])([a-zA-Z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
matches = re.finditer(regex, products)
total_calories = 0
for match in matches:
    total_calories += int(match.groups()[3])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
matches = re.finditer(regex, products)
for match in matches:
    sep, item_name, expiration_date, calories = match.groups()
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")



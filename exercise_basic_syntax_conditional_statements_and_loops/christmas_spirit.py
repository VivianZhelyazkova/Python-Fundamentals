decorations_quantity = int(input())
days_left = int(input())
budget = 0
spirit = 0
ornaments_price = 2
ornaments_spirit = 5
skirt_price = 5
skirt_spirit = 3
garland_price = 3
garland_spirit = 10
lights_price = 15
lights_spirit = 17

for day in range(1, days_left + 1):
    if day % 11 == 0:
        decorations_quantity += 2
    if day % 2 == 0:
        budget += ornaments_price * decorations_quantity
        spirit += ornaments_spirit
    if day % 3 == 0:
        budget += (skirt_price + garland_price) * decorations_quantity
        spirit += garland_spirit + skirt_spirit
    if day % 5 == 0:
        budget += lights_price * decorations_quantity
        spirit += lights_spirit
    if day % 3 == 0 and day % 5 == 0:
        spirit += 30
    if day % 10 == 0:
        spirit -= 20
        budget += skirt_price + garland_price + lights_price
if days_left % 10 == 0:
    spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")



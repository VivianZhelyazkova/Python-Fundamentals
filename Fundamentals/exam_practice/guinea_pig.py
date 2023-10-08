# quantity per 30 days
food_quantity_kg = float(input())
hay_quantity_kg = float(input())
cover_quantity_kg = float(input())
pet_weight_kg = float(input())
is_enough = True
food_quantity_gr = food_quantity_kg * 1000
hay_quantity_gr = hay_quantity_kg * 1000
cover_quantity_gr = cover_quantity_kg * 1000
pet_weight_gr = pet_weight_kg * 1000

for day in range(1, 30 + 1):
    food_quantity_gr -= 300
    if day % 2 == 0:
        hay_quantity_gr -= food_quantity_gr * 0.05
    if day % 3 == 0:
        cover_quantity_gr -= pet_weight_gr / 3
    if food_quantity_gr <= 0 or hay_quantity_gr <= 0 or cover_quantity_gr <= 0:
        print("Merry must go to the pet store!")
        is_enough = False
        break

if is_enough:
    print(f"Everything is fine! Puppy is happy!"
          f" Food: {(food_quantity_gr / 1000):.2f},"
          f" Hay: {(hay_quantity_gr / 1000):.2f},"
          f" Cover: {(cover_quantity_gr / 1000):.2f}.")

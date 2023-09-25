budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_liter = flour_price * 1.25
milk_price = milk_liter / 4
loaf_price = flour_price + eggs_price + milk_price
colored_eggs = 0
loaf_count = 0
while budget >= loaf_price:
    budget -= loaf_price
    loaf_count += 1
    colored_eggs += 3
    if loaf_count % 3 == 0:
        colored_eggs -= loaf_count - 2

budget_left = budget - (loaf_count * loaf_price)
print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")



days = int(input())
players = int(input())
group_energy = float(input())
water = float(input())
food = float(input())

total_water = water * players * days
total_food = food * players * days

for day in range(1,days + 1):
    chopping_wood = float(input())
    group_energy -= chopping_wood

    if group_energy <= 0:
        break
    if day % 2 == 0:
        group_energy *= 1.05
        total_water *= 0.7
    if day % 3 == 0:
        group_energy *= 1.1
        total_food -= total_food / players

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")



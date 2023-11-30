number = int(input())

plants = {}
RATING = "rating"
RARITY = "rarity"
for line in range(number):
    plant, rarity = input().split("<->")
    plants[plant] = {RARITY: rarity, RATING: []}

command = input()

while command != "Exhibition":
    cmd, info = command.split(": ")

    if info.split(" - ")[0] not in plants:
        print("error")
        command = input()
        continue
    if "Rate" in command:
        plant, rating = info.split(" - ")
        rating = int(rating)
        plants[plant][RATING].append(rating)
    elif "Update" in command:
        plant, new_rarity = info.split(" - ")
        plants[plant][RARITY] = new_rarity
    elif "Reset" in command:
        plant = info
        plants[plant][RATING].clear()
    command = input()

print("Plants for the exhibition: ")

for plant, info in plants.items():
    if len(info[RATING]) == 0:
        average_rating = 0.00
    else:
        average_rating = sum(info[RATING]) / len(info[RATING])
    print(f"- {plant}; Rarity: {info[RARITY]}; Rating: {average_rating:.2f}")

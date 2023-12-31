command = input()
cities = {}
while command != "Sail":
    city, population, gold = command.split("||")[0], int(command.split("||")[1]), int(command.split("||")[2])
    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold
    command = input()

event = input()

while event != "End":
    if "Plunder" in event:
        town, people, gold = event.split("=>")[1], int(event.split("=>")[2]), int(event.split("=>")[3])
        cities[town][0] -= people
        cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif "Prosper" in event:
        town, gold = event.split("=>")[1],int(event.split("=>")[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            event = input()
            continue
        cities[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
    event = input()

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to: ")
    for city, info in cities.items():
        print(f"{city} -> Population: {info[0]} citizens, Gold: {info[1]} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

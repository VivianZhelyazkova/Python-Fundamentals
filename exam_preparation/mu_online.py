initial_health = 100
initial_bitcoins = 0

dungeon_rooms = input().split("|")
success = True

for index, room in enumerate(dungeon_rooms):
    command, number = room.split()
    number = int(number)
    if command == "potion":
        initial_health += number
        healed_amount = number
        if initial_health > 100:
            healed_amount = number - (initial_health - 100)
            initial_health = 100
        print(f"You healed for {healed_amount} hp.\n"
              f"Current health: {initial_health} hp.")
    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        initial_health -= number
        if initial_health > 0:
            print(f"You slayed {command}.")

        else:
            print(f"You died! Killed by {command}.\n"
                  f"Best room: {index + 1}")
            success = False
            break
if success:
    print(f"You've made it!\n"
          f"Bitcoins: {initial_bitcoins}\n"
          f"Health: {initial_health}")

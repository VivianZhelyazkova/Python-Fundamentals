initial_energy = 100
initial_coins = 100

list_of_events = input().split('|')
bakery_opened = True

for event in list_of_events:
    command, number = event.split("-")
    number = int(number)
    if command == "rest":
        current_energy = initial_energy
        initial_energy += number
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif command == "order":
        if initial_energy < 30:
            initial_energy += 50
            print(f"You had to rest!")
        else:
            initial_coins += number
            initial_energy -= 30
            print(f"You earned {number} coins.")
    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            bakery_opened = False
            break
if bakery_opened:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")

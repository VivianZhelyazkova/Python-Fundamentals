initial_energy = int(input())
wins = 0
command = input()

while command != 'End of battle':
    distance = int(command)
    if initial_energy >= distance:
        initial_energy -= distance
        wins += 1
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy} energy")
        break
    if wins % 3 == 0:
        initial_energy += wins
    command = input()

if command == "End of battle":
    print(f"Won battles: {wins}. Energy left: {initial_energy}")
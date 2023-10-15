targets = [int(i) for i in input().split()]
command = input()

while command != "End":
    command, index, value = command.split()
    index = int(index)
    value = int(value)
    if "Shoot" in command:
        if index in range(len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif "Add" in command:
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")
    elif "Strike" in command:
        if index in range(len(targets)):
            if index - value not in range(len(targets)) or index + value not in range(len(targets)):
                print(f"Strike missed!")
                command = input()
                continue
            else:
                del targets[index - value: index + value + 1]
    command = input()

if command == "End":
    print(*targets, sep="|")







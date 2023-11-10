number_of_wagons = [0 for x in range(int(input()))]
command = input()

while command != 'End':
    if "add" in command:
        cmd, people = command.split()
        people = int(people)
        number_of_wagons[len(number_of_wagons) - 1] += people
    elif "insert" in command:
        cmd, index, people = command.split()
        index = int(index)
        people = int(people)
        number_of_wagons[index] += people
    elif "leave" in command:
        cmd, index, people = command.split()
        index = int(index)
        people = int(people)
        number_of_wagons[index] -= people
    command = input()

print(number_of_wagons)
numbers = [int(x) for x in input().split()]
command = input()

while command != "end":
    command = command.split()
    if "swap" in command:
        first_index = int(command[1])
        second_index = int(command[2])
        numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]
    elif "multiply" in command:
        first_index = int(command[1])
        second_index = int(command[2])
        numbers[first_index] = numbers[first_index] * numbers[second_index]
    elif "decrease":
        numbers = list(map(lambda x: x - 1, numbers))
    command = input()


print(", ".join([str(x) for x in numbers]))


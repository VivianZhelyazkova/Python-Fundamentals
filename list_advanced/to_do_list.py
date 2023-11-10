command = input()
list_of_commands = []
while command != "End":
    list_of_commands.append(command)
    command = input()

sorted_commands = [x.split("-")[1] for x in sorted(list_of_commands, key=lambda x: int(x.split("-")[0]))]

print(sorted_commands)
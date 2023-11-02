command = input()
phonebook = {}
while "-" in command:

    name, number = command.split("-")
    phonebook[name] = number
    command = input()

searches = int(command)

for search in range(searches):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

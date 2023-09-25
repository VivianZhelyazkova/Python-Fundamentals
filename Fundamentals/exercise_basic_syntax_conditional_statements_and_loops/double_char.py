command = input()

while command != "End":
    doubled_string = ""
    if command == "SoftUni":
        continue
    for char in command:
        doubled_string += char * 2
    print(doubled_string)
    if command == "End":
        break
    command = input()
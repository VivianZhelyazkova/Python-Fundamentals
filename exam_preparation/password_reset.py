password = input()
command = input()

while command != "Done":
    if "TakeOdd" in command:
        password = "".join(list(char for index, char in enumerate(password) if index % 2 != 0))
        print(password)
    elif "Cut" in command:
        cmd, index, length = command.split()
        index = int(index)
        length = int(length)
        part_to_remove = password[index:index + length]
        password = password.replace(part_to_remove, "", 1)
        print(password)
    elif "Substitute" in command:
        cmd, substring, substitute = command.split()
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")

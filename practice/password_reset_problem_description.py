password = input()

command = input()

while command != "Done":

    if "TakeOdd" in command:
        password = "".join([char for index, char in enumerate(password) if index % 2 != 0])
        print(password)

    elif "Cut" in command:
        index, length = int(command.split()[1]), int(command.split()[2])
        substring = password[index:index + length]
        password = password.replace(substring, "", 1)
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

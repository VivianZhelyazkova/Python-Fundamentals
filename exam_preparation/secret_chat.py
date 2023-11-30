concealed_message = input()

string = input()

while string != "Reveal":
    if "InsertSpace" in string:
        instruction, index = string.split(":|:")
        index = int(index)
        first_part = concealed_message[:index]
        second_part = concealed_message[index:]
        concealed_message = first_part + " " + second_part
        print(concealed_message)
    elif "Reverse" in string:
        instruction, substring = string.split(":|:")
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            substring_rev = substring[::-1]
            concealed_message += substring_rev
            print(concealed_message)
        else:
            print("error")

    elif "ChangeAll" in string:
        instruction, substring, replacement = string.split(":|:")
        concealed_message = concealed_message.replace(substring,replacement)
        print(concealed_message)
    string = input()

print(f"You have a new text message: {concealed_message}")
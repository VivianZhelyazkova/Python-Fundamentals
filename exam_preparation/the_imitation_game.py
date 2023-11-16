encrypted_message = input()
command = input()

while command != "Decode":
    if "Move" in command:
        cmd, number = command.split("|")
        number = int(number)
        part_to_move = encrypted_message[:number]
        encrypted_message = encrypted_message[number:] + part_to_move
    elif "Insert" in command:
        cmd, index, value = command.split("|")
        index = int(index)
        first_part = encrypted_message[:index]
        second_part = encrypted_message[index:]
        encrypted_message = first_part + value + second_part
    elif "ChangeAll" in command:
        cmd, substring, replacement = command.split("|")
        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")

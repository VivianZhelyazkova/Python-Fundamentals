list_of_phones = input().split(", ")
command = input()

while command != "End":
    phone = command.split(" - ")[1]
    if "Add" in command:
        if phone not in list_of_phones:
            list_of_phones.append(phone)
    if "Remove" in command:
        if phone in list_of_phones:
            list_of_phones.remove(phone)
    if "Bonus phone" in command:
        old_phone, new_phone = phone.split(":")
        if old_phone in list_of_phones:
            list_of_phones.insert(list_of_phones.index(old_phone) + 1, new_phone)
    if "Last" in command:
        if phone in list_of_phones:
            list_of_phones.remove(phone)
            list_of_phones.append(phone)

    command = input()
print(", ".join(list_of_phones))


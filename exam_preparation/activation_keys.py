raw_key = input()
command = input()

while command != "Generate":
    if "Contains" in command:
        cmd, substring = command.split(">>>")
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif "Flip" in command:
        cmd, upper_lower, start_index, end_index = command.split(">>>")
        start_index = int(start_index)
        end_index = int(end_index)
        first_part = raw_key[:start_index]
        second_part = raw_key[end_index:]
        if upper_lower == "Upper":
            part_to_change = raw_key[start_index:end_index].upper()
        elif upper_lower == "Lower":
            part_to_change = raw_key[start_index:end_index].lower()
        raw_key = first_part + part_to_change + second_part
        print(raw_key)
    elif "Slice" in command:
        cmd, start_index, end_index = command.split(">>>")
        start_index = int(start_index)
        end_index = int(end_index)
        part_to_delete = raw_key[start_index:end_index]
        raw_key = raw_key.replace(part_to_delete, "")
        print(raw_key)
    command = input()

print(f"Your activation key is: {raw_key}")

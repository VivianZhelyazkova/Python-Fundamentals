stops = input()

command = input()

while command != "Travel":
    if "Add" in command:
        cmd, index, string = command.split(":")
        index = int(index)
        if index in range(len(stops)):
            first_part = stops[:index]
            second_part = stops[index:]
            stops = first_part + string + second_part
        print(stops)
    elif "Remove" in command:
        cmd, start, end = command.split(":")
        start = int(start)
        end = int(end)
        if start in range(len(stops)) and end in range(len(stops)):
            first_part = stops[:start]
            second_part = stops[end + 1:]
            stops = first_part + second_part
        print(stops)
    elif "Switch" in command:
        cmd, old_string, new_string = command.split(":")
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")

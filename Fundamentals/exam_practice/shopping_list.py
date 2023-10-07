initial_list = input().split("!")
command = input()

while command != "Go Shopping!":
    if "Urgent" in command:
        cmd, item = command.split()
        if item not in initial_list:
            initial_list.insert(0, item)
    elif "Unnecessary" in command:
        cmd, item = command.split()
        if item in initial_list:
            initial_list.remove(item)
    elif "Correct" in command:
        cmd, old_item, new_item = command.split()
        if old_item in initial_list:
            initial_list[initial_list.index(old_item)] = new_item
    elif "Rearrange" in command:
        cmd, item = command.split()
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)
    command = input()

print(*initial_list, sep=", ")








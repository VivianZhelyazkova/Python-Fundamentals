inventory = input().split(", ")
command = input()

while command != "Craft!":
    cmd, item = command.split(" - ")
    if "Collect" in command:
        if item not in inventory:
            inventory.append(item)
    elif "Drop" in command:
        if item in inventory:
            inventory.remove(item)
    elif "Combine Items" in command:
        old_item, new_item = item.split(":")
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)
    elif "Renew" in command:
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    command = input()

print(*inventory, sep=", ")

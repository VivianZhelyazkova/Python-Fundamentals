initial_loot = input().split("|")
command = input()

while command != "Yohoho!":
    if "Loot" in command:
        looted_items = command.split()
        looted_items.remove("Loot")
        for item in looted_items:
            if item not in initial_loot:
                initial_loot.insert(0, item)
    if "Drop" in command:
        cmd, index = command.split()
        index = int(index)
        if 0 <= index < len(initial_loot):
            item_to_drop = initial_loot.pop(index)
            initial_loot.append(item_to_drop)
    if "Steal" in command:
        cmd, count = command.split()
        count = int(count)
        stolen_loot = []
        if count >= len(initial_loot):
            stolen_loot = initial_loot.copy()
            initial_loot.clear()
        else:
            stolen_loot = initial_loot[- count:]
            initial_loot = initial_loot[:- count]
        print(", ".join(stolen_loot))
    command = input()

if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    sum_of_items = 0
    for item in initial_loot:
        sum_of_items += len(item)
    average = sum_of_items / len(initial_loot)
    print(f"Average treasure gain: {average:.2f} pirate credits.")

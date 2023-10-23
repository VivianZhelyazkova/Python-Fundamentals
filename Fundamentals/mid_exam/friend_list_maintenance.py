friends = input().split(", ")
command = input()

while command != "Report":
    if "Blacklist" in command:
        cmd, name = command.split()
        if name in friends:
            print(f"{name} was blacklisted.")
            friends[friends.index(name)] = "Blacklisted"
        else:
            print(f"{name} was not found.")
    if "Error" in command:
        cmd, index = command.split()
        index = int(index)
        if index in range(len(friends)) and friends[index] != "Blacklisted" and friends[index] != "Lost":
            print(f"{friends[index]} was lost due to an error.")
            friends[index] = "Lost"
    if "Change" in command:
        cmd, index, new_name = command.split()
        index = int(index)
        if index in range(len(friends)):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name
    command = input()

print(f"Blacklisted names: {friends.count('Blacklisted')}")
print(f"Lost names: {friends.count('Lost')}")
print(" ".join(friends))

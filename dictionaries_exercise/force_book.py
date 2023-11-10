command = input()

sides = {}


def add_or_transfer_user(user, user_side, sides_dict, should_append):
    found = any(user in value_list for value_list in sides_dict.values())
    if found:
        for key, value in sides_dict.items():
            if user in value:
                value.remove(user)
        sides_dict[user_side].append(user)
    else:
        if should_append:
            sides[side].append(name)
        else:
            sides_dict[user_side] = [user]
    print(f"{user} joins the {user_side} side!")


while command != "Lumpawaroo":
    if "|" in command:
        side, name = command.split(" | ")
        if side not in sides:
            sides[side] = []
        found = any(name in value_list for value_list in sides.values())
        if not found:
            sides[side].append(name)
    if "->" in command:
        name, side = command.split(" -> ")
        if side not in sides:
            sides[side] = []
            add_or_transfer_user(name, side, sides, False)
        else:
            add_or_transfer_user(name, side, sides, True)

    command = input()

for side, members in sides.items():
    if len(members) > 0:
        print(f"Side: {side}, Members: {len(members)}")
        for member in members:
            print(f"! {member}")

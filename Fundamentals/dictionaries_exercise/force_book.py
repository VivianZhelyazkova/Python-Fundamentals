command = input()

sides = {}

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
            found = any(name in value_list for value_list in sides.values())
            if found:
                for key, value in sides.items():
                    if name in value:
                        value.remove(name)
                sides[side].append(name)
            else:
                sides[side] = [name]
            print(f"{name} joins the {side} side!")
        else:
            found = any(name in value_list for value_list in sides.values())
            if found:
                for key, value in sides.items():
                    if name in value:
                        value.remove(name)
                sides[side].append(name)
            else:
                sides[side].append(name)
            print(f"{name} joins the {side} side!")
    command = input()

print(sides)

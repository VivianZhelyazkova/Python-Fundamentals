command = input()

dwarfs_data = {}
dwarfs_count = {}

while command != "Once upon a time":
    name, hat_color, physics = command.split(" <:> ")
    physics = int(physics)
    dwarf_key = (name, hat_color)
    if dwarf_key in dwarfs_data:
        if physics > dwarfs_data[dwarf_key]:
            dwarfs_data[dwarf_key] = physics
    else:
        dwarfs_data[dwarf_key] = physics

    if hat_color in dwarfs_count:
        dwarfs_count[hat_color] += 1
    else:
        dwarfs_count[hat_color] = 1
    command = input()

sorted_dwarfs = sorted(dwarfs_data.items(), key=lambda x: (-x[1], -dwarfs_count[x[0][1]]))

for (name, hat_color), physics in sorted_dwarfs:
    print(f"({hat_color}) {name} <-> {physics}")

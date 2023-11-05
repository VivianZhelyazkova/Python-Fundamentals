number = int(input())

vivis_dragons = {}

for dragon in range(number):
    dragon_type, name, damage, health, armor = input().split()

    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    damage = int(damage)
    health = int(health)
    armor = int(armor)

    if dragon_type not in vivis_dragons:
        vivis_dragons[dragon_type] = {name: [damage, health, armor]}
    else:
        vivis_dragons[dragon_type][name] = [damage, health, armor]

for dragon_type, info in vivis_dragons.items():
    average_damage = sum([dragon[0] for dragon in info.values()]) / len(info)
    average_health = sum([dragon[1] for dragon in info.values()]) / len(info)
    average_armor = sum([dragon[2] for dragon in info.values()]) / len(info)
    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    sorted_names = dict(sorted(vivis_dragons[dragon_type].items(), key=lambda x: x[0]))
    for name, data in sorted_names.items():
        print(f"-{name} -> damage: {data[0]}, health: {data[1]}, armor: {data[2]}")

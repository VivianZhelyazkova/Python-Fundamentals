wanted_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

legendary_obtained = False

while not legendary_obtained:

    line = input().lower().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1]
        if material in wanted_materials:
            wanted_materials[material] += quantity
            if wanted_materials[material] >= 250:
                legendary_obtained = True
                legendary_item = legendary_items[material]
                print(f"{legendary_item} obtained!")
                wanted_materials[material] -= 250
                break
        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity

for material, quantity in wanted_materials.items():
    print(f"{material}: {quantity}")
for trashka, quantity in junk.items():
    print(f"{trashka}: {quantity}")

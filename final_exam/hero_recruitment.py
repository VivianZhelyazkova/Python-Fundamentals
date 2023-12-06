command = input()
heroes = {}


while command != "End":
    if "Enroll" in command:
        cmd, hero_name = command.split()
        if hero_name in heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []
    elif "Learn" in command:
        cmd, hero_name, spell_name = command.split()
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes[hero_name].append(spell_name)
    elif "Unlearn" in command:
        cmd, hero_name, spell_name = command.split()
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name not in heroes[hero_name]:
                print(f"{hero_name} doesn't know {spell_name}.")
            else:
                heroes[hero_name].remove(spell_name)
    command = input()

print("Heroes:")

for hero, spells in heroes.items():
    print(f"== {hero}: {', '.join(spells)}")

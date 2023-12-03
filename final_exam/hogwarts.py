spell = input()

command = input()

while command != "Abracadabra":
    if command == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif command == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif "Illusion" in command:
        cmd, index, letter = command.split()
        index = int(index)
        if index in range(len(spell)):
            spell = list(spell)
            spell[index] = letter
            spell = "".join(spell)
            print("Done!")
        else:
            print("The spell was too weak.")
    elif "Divination" in command:
        cmd, first_sub, second_sub = command.split()
        if first_sub in spell:
            spell = spell.replace(first_sub, second_sub)
            print(spell)
    elif "Alteration" in command:
        cmd, substring = command.split()
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
    else:
        print("The spell did not work!")
    command = input()


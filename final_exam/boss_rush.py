import re

number = int(input())

for line in range(number):
    boss = input()
    regex = r"\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#"
    matches = re.finditer(regex, boss)
    if matches:
        for match in matches:
            name = match.group(1)
            title = match.group(2)
            print(f"{name}, The {title}\n"
                  f">> Strength: {len(name)}\n"
                  f">> Armor: {len(title)}")
    else:
        print("Access denied!")

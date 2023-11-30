import re

string = input()

regex = r"([@#]){1}([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
matches = re.finditer(regex, string)

pairs = []
mirrored_pairs = []

for match in matches:
    if match.group(2) == match.group(3)[::-1]:
        mirrored_pairs.append(match.group(2) + " <=> " + match.group(3))
    pairs.append(match)

if pairs:
    print(f"{len(pairs)} word pairs found!")
else:
    print("No word pairs found!")

if mirrored_pairs:
    print("The mirror words are: ")
    print(", ".join(mirrored_pairs))
else:
    print("No mirror words!")

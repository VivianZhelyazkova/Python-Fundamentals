# import math
import re

text = input()

numbers = list(int(x) for x in text if x.isdigit())
# threshold = math.prod(numbers)
threshold = 1
for number in numbers:
    threshold *= number

regex = r"([:]{2}|[*]{2})([A-Z][a-z]{2,})(\1)"
matches = re.finditer(regex, text)

emojies = []
cool_emojies = []

for match in matches:
    emojies.append(match.group(2))
    ascii_sum = sum(list(ord(x) for x in match.group(2)))
    if ascii_sum >= threshold:
        cool_emojies.append("".join(match.groups()))

print(f"Cool threshold: {threshold}")
print(f"{len(emojies)} emojis found in the text. The cool ones are: ")

for emoji in cool_emojies:
    print(emoji)

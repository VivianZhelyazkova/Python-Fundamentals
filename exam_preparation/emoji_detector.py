import math
import re

text = input()

numbers = list(int(x) for x in text if x.isnumeric())
threshold = math.prod(numbers)
print(threshold)

regex = r"([:*]{2})([A-Z][a-z]{2,})\1"
matches = re.finditer(regex, text)

emojies = []
cool_emojies = []

for match in matches:
    emojies.append(match.group(2))


import re

numbers = []
while True:

    line = input()
    if not line:
        break
    else:
        regex = "\\d+"
        numbers.extend(re.findall(regex, line))

print(" ".join(numbers))

import re

numbers = input()
regex = "(^|(?<=\\s))-?([0]|[1-9][0-9]*)(\\.\\d+)?($|(?=\\s))"
matches = re.finditer(regex, numbers)

for match in matches:
    print(match.group(), end=" ")

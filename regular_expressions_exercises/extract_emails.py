import re

text = input()
regex = "(^|(?<=\\s))(([a-zA-Z0-9]+)([.-]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([.-][A-Za-z]+)+))(\\b|(?=\\s))"
matches = re.finditer(regex, text)

for match in matches:
    print(match.group())

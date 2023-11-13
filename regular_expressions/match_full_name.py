import re

regex = "(\\+359-2-\\d{3}-\\d{4}|\\+359 2 \\d{3} \\d{4})\\b"
numbers = input()
matches = re.findall(regex, numbers)
print(", ".join(matches))

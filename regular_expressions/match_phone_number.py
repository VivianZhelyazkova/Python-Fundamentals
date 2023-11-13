import re

numbers = input()
regex = r"\\b(?:\\+359\\s?2(?:-|\\s)?\\d{3}(?:-|\\s)?\\d{4})\\b"
matches = re.findall(regex, numbers)
print(", ".join(matches))
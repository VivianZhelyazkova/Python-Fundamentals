import re

string = input().lower()
word_to_find = input().lower()
regex = f"\\b{word_to_find}\\b"
# pattern = re.compile(r'\b' + re.escape(word_to_find) + r'\b', re.IGNORECASE)

matches = re.findall(regex, string)
count = len(matches)
print(count)

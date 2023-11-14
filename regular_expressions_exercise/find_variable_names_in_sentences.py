import re

string = input()
regex = "\\b_[a-zA-Z]+\\b"
matches = re.findall(regex, string)

filtered = [word.strip("_") for word in matches]
print(",".join(filtered))

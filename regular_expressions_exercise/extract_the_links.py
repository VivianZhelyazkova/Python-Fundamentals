import re

string = input()
regex = "\\bw{3}.[a-zA-Z0-9\\-]+\\.[a-z]+(?:.[a-z]+)+\\b"

while True:
    if not string:
        break
    valid_link = re.findall(regex, string)
    if valid_link:
        print("".join(valid_link))
    string = input()

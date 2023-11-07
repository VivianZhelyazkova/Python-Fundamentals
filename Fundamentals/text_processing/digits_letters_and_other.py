string = input()

digits = ""
letters = ""
characters = ""

for char in string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        characters += char

print(digits)
print(letters)
print(characters)
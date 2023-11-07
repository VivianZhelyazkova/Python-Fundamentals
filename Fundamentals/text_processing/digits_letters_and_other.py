string = input()

digits = "".join([char for char in string if char.isdigit()])
letters = "".join([char for char in string if char.isalpha()])
characters = "".join([char for char in string if not char.isalnum()])

# for char in string:
#     if char.isdigit():
#         digits += char
#     elif char.isalpha():
#         letters += char
#     else:
#         characters += char

print(digits)
print(letters)
print(characters)
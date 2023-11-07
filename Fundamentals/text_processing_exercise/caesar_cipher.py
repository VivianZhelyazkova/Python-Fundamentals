text = input()

# encrypted = ""
#
# for char in text:
#
#     encrypted += chr(ord(char) + 3)

encrypted = "".join(chr(ord(char) + 3) for char in text)
print(encrypted)

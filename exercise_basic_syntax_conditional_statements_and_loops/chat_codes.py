lines_number = int(input())
message = ""
for number in range(lines_number):
    current = int(input())
    if current == 88:
        message  = "Hello"
    elif current == 86:
        message = "How are you?"
    elif current < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(message)
first_char = input()
second_char = input()
third_char = input()


def string(first, second, third):
    result = f"{first_char}{second_char}{third_char}"
    return result


chars_as_string = string(first_char, second_char, third_char)
print(chars_as_string)

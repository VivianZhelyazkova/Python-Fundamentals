password = list(input())
ASCII_DIGITS_RANGE = range(48, 57 + 1)
ASCII_UPPER_LETTERS_RANGE = range(65, 90 + 1)
ASCII_LOWER_LETTERS_RANGE = range(97, 122 + 1)

def is_valid(pswd):
    valid = True
    is_in_range = True
    digit_counter = 0
    if len(pswd) not in range(6, 10 + 1):
        print("Password must be between 6 and 10 characters")
        valid = False
    for digit in pswd:
        digit_as_ascii = ord(digit)
        if digit_as_ascii in ASCII_DIGITS_RANGE:
            digit_counter += 1
        if digit_as_ascii not in ASCII_DIGITS_RANGE\
                and digit_as_ascii not in ASCII_UPPER_LETTERS_RANGE \
                and digit_as_ascii not in ASCII_LOWER_LETTERS_RANGE:
            is_in_range = False
            valid = False
    if not is_in_range:
        print("Password must consist only of letters and digits")

    if digit_counter < 2:
        print("Password must have at least 2 digits")
        valid = False
    return valid


if is_valid(password):
    print("Password is valid")


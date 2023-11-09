from enum import Enum

strings = input().split()
results = []


class Operation(Enum):
    DIVIDE = 1
    MULTIPLY = 2
    SUBTRACT = 3
    ADD = 4


def result(letter, num, max_res, operation: Operation):
    letter_value = ord(letter.lower()) - 96
    current_result = 0
    match operation:
        case Operation.DIVIDE:
            current_result = num / letter_value
        case Operation.MULTIPLY:
            current_result = num * letter_value
        case Operation.SUBTRACT:
            current_result = max_res - letter_value
        case Operation.ADD:
            current_result = max_res + letter_value
    return current_result


for string in strings:
    max_result = 0
    number = int("".join(list(n for n in string if n.isdigit())))
    first_letter, second_letter = string[0], string[-1]
    if first_letter.isupper():
        max_result = result(first_letter, number, max_result, Operation.DIVIDE)
    elif first_letter.islower():
        max_result = result(first_letter, number, max_result, Operation.MULTIPLY)
    if second_letter.isupper():
        max_result = result(second_letter, number, max_result, Operation.SUBTRACT)
    elif second_letter.islower():
        max_result = result(second_letter, number, max_result, Operation.ADD)
    results.append(max_result)

print(f"{sum(results):.2f}")

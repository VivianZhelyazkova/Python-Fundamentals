strings = input().split()
results = []
for string in strings:
    max_result = 0
    number = int("".join(list(n for n in string if n.isdigit())))
    first_letter, second_letter = string[0], string[-1]
    if first_letter.isupper():
        letter_lower = first_letter.lower()
        letter_value = ord(letter_lower) - 96
        current_result = number / letter_value
        max_result = max(current_result, max_result)
    elif first_letter.islower():
        letter_lower = first_letter.lower()
        letter_value = ord(letter_lower) - 96
        current_result = number * letter_value
        max_result = max(current_result, max_result)
    if second_letter.isupper():
        letter_lower = second_letter.lower()
        letter_value = ord(letter_lower) - 96
        current_result = max_result - letter_value
        max_result = current_result
    elif second_letter.islower():
        letter_lower = second_letter.lower()
        letter_value = ord(letter_lower) - 96
        current_result = max_result + letter_value
        max_result = current_result
    results.append(max_result)

print(f"{sum(results):.2f}")

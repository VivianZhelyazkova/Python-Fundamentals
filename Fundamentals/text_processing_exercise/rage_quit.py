text = input().upper()

parts = [""] * len(text)
current_index = 0
counting_digits = False
for index, char in enumerate(text):

    if not char.isdigit():
        if counting_digits:
            counting_digits = False
            current_index += 1
        parts[current_index] += char
    else:
        counting_digits = True
        parts[current_index] += char
parts = list(filter(lambda x: x != "", parts))
final_message = ""
for part in parts:
    message = "".join(list(char for char in part if not char.isdigit()))
    repeats = int("".join(list(char for char in part if char.isdigit())))
    final_message += message * repeats
unique_symbols = len(set(final_message))
print(f"Unique symbols used: {unique_symbols}")
print(final_message)
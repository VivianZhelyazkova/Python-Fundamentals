message = input().split()
deciphered_message = []
for current_word in message:
    word = list(current_word)
    numbers = int("".join([x for x in word if x.isnumeric()]))
    characters = [x for x in word if not x.isnumeric()]
    first_part = chr(numbers)
    characters[0], characters[len(characters) - 1] = characters[len(characters) - 1], characters[0]
    deciphered_word = first_part + "".join(characters)
    deciphered_message.append(deciphered_word)

print(" ".join(deciphered_message))


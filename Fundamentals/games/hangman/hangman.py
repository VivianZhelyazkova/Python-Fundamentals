from drawing_util import draw_hangman
from data_util import get_random_word
secret_word = get_random_word()
remaining_lives = 7
guessed_word = []

for i in secret_word:
    guessed_word.append("_")
print("".join(guessed_word))

while "_" in guessed_word and remaining_lives > 0:

    guessed_letter = input("Guess a letter\n")
    if guessed_letter not in secret_word:
        remaining_lives -= 1
        draw_hangman(remaining_lives)

    for index, element in enumerate(secret_word):
        if guessed_letter == element:
            guessed_word[index] = element
    print("".join(guessed_word))
    print(f"You have {remaining_lives} tries left.\n")

if remaining_lives <= 0:
    print("Leka trashka")
else:
    print("You got it!")



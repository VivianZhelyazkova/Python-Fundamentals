from random import randint
guess = int(input("Guess a number\n"))
secret_number = randint(1,100)
while guess != secret_number:
    if guess > secret_number:
        print("Your number is too big")
    elif guess < secret_number:
        print("Your number is too small")
    guess = int(input("Guess a number\n"))

print(f"Congratulations! You guessed my number! It is {secret_number}")

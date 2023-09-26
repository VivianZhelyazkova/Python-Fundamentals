from random import randint


def get_random_word():
    random_words = ["apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
                    "computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor",
                    "softuni"]
    random_index = randint(0, len(random_words) - 1)
    secret_word = random_words[random_index]
    return secret_word

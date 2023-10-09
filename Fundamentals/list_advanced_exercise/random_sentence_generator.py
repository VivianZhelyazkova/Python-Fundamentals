import random

names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
details = ["near the river", "at home", "in the park"]


def get_random_word(some_list):
    return random.choice(some_list)


print("Hello, this is your first random sentence:")

while True:
    random_sentence = (f"{get_random_word(names)} form {get_random_word(places)} {get_random_word(adverbs)}"
                       f" {get_random_word(verbs)} {get_random_word(nouns)} {get_random_word(details)}.")
    print(random_sentence)
    input("Click [Enter] to generate a new one.")

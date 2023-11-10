first_character = input()
second_character = input()


def string(f,s):
    list_of_characters = []
    f_as_int = ord(f)
    s_as_int = ord(s)
    for i in range(f_as_int + 1, s_as_int):
        character = chr(i)
        list_of_characters.append(character)
    return list_of_characters


print(" ".join(string(first_character, second_character)))

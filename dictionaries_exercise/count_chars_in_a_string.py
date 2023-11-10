string = list(input())

my_dict = {}

for char in string:
    if char not in my_dict.keys() and char != " ":
        my_dict[char] = 1
    elif char in my_dict.keys() and char != " ":
        my_dict[char] += 1

for char, occurrences in my_dict.items():
    print(f"{char} -> {occurrences}")


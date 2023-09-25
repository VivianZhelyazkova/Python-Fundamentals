
coffe_count = 0
while True:
    command = input()
    if command == "END":
        break
    # if command == "dog" or command == "cat" or command == "coding" or command == "movie":
    #     if command.islower():
    #         coffe_count += 1
    #     else:
    #         coffe_count += 2
    if command in ["dog", "cat", "coding", "movie"]:
        if command.islower():
            coffe_count += 1
        else:
            coffe_count += 2
    if command != "dog" or command != "cat" or command != "coding" or command != "movie":
        continue


if coffe_count > 5:
    print("You need extra sleep")
else:
    print(coffe_count)
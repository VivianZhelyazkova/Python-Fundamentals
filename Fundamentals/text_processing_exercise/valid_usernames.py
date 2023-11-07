line = input().split(", ")

for user in line:

    if len(user) in range(3, 17):
        is_valid = True
        for char in user:
            if not char.isalnum() and char != "-" and char != "_":
                is_valid = False

        if is_valid:
            print(user)

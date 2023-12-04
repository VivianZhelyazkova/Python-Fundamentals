line = input().split(", ")

valid_users = []

for user in line:

    if len(user) in range(3, 17):
        is_valid = True
        for char in user:
            if not char.isalnum() and char != "-" and char != "_":
                is_valid = False

        if is_valid:
            print(user)

# line_copy = line.copy()
# for user in line:
#
#     if len(user) in range(3, 17):
#         for char in user:
#             if not char.isalnum() and char != "-" and char != "_":
#                 line_copy.remove(user)
#     if len(user) not in range(3, 17):
#         line_copy.remove(user)
#
# print(line_copy)
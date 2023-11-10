x = 6
y = 5

#     *
#     *
#   ***
#  ****
# *****
for vertical in range(y):
    for horizontal in range(y - vertical + 1):
        print(" ", end ="")
    for horizontal_star in range(vertical + 1):
        print("*", end = "")
    print()

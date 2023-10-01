first_line = input().split()
second_line = input().split()
third_line = input().split()


def check_for_win(digit):
    if digit == "1":
        print("First player won")
        exit()
    if digit == "2":
        print("Second player won")
        exit()


# checking horizontal lines
if first_line[0] == first_line[1] and first_line[1] == first_line[2]:
    check_for_win(first_line[0])
elif second_line[0] == second_line[1] and second_line[1] == second_line[2]:
    check_for_win(second_line[0])
elif third_line[0] == third_line[1] and third_line[1] == third_line[2]:
    check_for_win(third_line[0])

# checking vertical lines
if first_line[0] == second_line[0] and second_line[0] == third_line[0]:
    check_for_win(first_line[0])
elif first_line[1] == second_line[1] and second_line[1] == third_line[1]:
    check_for_win(first_line[1])
elif first_line[2] == second_line[2] and second_line[2] == third_line[2]:
    check_for_win(first_line[2])

# checking diagonal lines
if first_line[0] == second_line[1] and second_line[1] == third_line[2]:
    check_for_win(first_line[0])
elif first_line[2] == second_line[1] and second_line[1] == third_line[0]:
    check_for_win(first_line[2])

print("Draw!")
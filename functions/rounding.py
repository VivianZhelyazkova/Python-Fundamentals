list_of_numbers = input().split(" ")


def round_a_number(n):
    rounded_number = round(n)
    return rounded_number


new_list = []

for number in list_of_numbers:
    new_list.append(round_a_number(float(number)))

print(new_list)

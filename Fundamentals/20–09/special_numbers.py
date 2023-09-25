number = int(input())

for i in range(1, number + 1):
    number_as_string = str(i)
    digit_sum = 0
    for digit in number_as_string:
        digit_sum += int(digit)
    is_special = False
    if digit_sum in [5, 7, 11]:
        is_special = True
    print(f"{i} -> {is_special}")


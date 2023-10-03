number = input()


def sum_of_even_and_odd(n):
    list_of_numbers = list(n)
    even_digits = []
    odd_digits = []
    for digit in list_of_numbers:
        digit = int(digit)
        if digit % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)
    odd_sum = sum(odd_digits)
    even_sum = sum(even_digits)
    string = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return string


print(sum_of_even_and_odd(number))

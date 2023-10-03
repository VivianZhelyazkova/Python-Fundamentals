list_of_numbers = input().split(", ")


def is_palindrome(lst):
    if len(lst) == 1:
        return True
    if len(lst) % 2 == 0:
        first_half = lst[:len(lst) // 2]
        second_half = lst[len(lst) // 2:]
        if first_half == second_half[::-1]:
            palindrome = True
        else:
            palindrome = False
    elif len(lst) % 2 != 0:
        first_half = lst[:len(lst) // 2]
        second_half = lst[len(lst) // 2 + 1:]
        if first_half == second_half[::-1]:
            palindrome = True
        else:
            palindrome = False
    return palindrome


for n in list_of_numbers:
    print(is_palindrome(n))


first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(f, s):
    result = f + s
    return result


def subtract(res, t):
    result = res - t
    return result


def add_and_subtract(f, s, t):
    print(subtract(sum_numbers(f, s), t))


add_and_subtract(first_number, second_number, third_number)

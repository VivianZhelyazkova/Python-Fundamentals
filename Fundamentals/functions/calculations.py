operator = input()
first_number = int(input())
second_number = int(input())


def solve(opr, first, second):
    if opr == 'multiply':
        result = first * second
    elif opr == 'divide':
        result = int(first / second)
    elif opr == 'add':
        result = first + second
    elif opr == 'subtract':
        result = first - second

    return result


print(solve(operator, first_number, second_number))
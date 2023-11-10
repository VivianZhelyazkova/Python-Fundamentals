first_number = int(input())
second_number = int(input())


def factorial(n):
    sum_n = 1
    for i in range(1, n + 1):
        sum_n *= i
    return sum_n


first_sum = factorial(first_number)
second_sum = factorial(second_number)
result = first_sum / second_sum

print(f"{result:.2f}")
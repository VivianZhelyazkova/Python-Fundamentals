number = int(input())


def is_perfect_number(n):
    if n <= 0:
        return "It's not so perfect."
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    if divisors_sum == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


result = is_perfect_number(number)
print(result)

numbers = [int(x) for x in input().split(", ")]

common_numbers = list(set(filter(lambda x: numbers.count(x) >= 3, numbers)))
consecutive_numbers = []
for number in common_numbers:
    index = numbers.index(number)
    if numbers[index] == numbers[index + 1] and numbers[index] == numbers[index + 2]:
        consecutive_numbers.append(number)

print(consecutive_numbers)

divisor = int(input())
boundary = int(input())

for number in range(boundary, 1, -1):
    if number % divisor == 0:
        print(number)
        break


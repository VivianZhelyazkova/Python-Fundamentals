import math

first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())


def hypotenuse(x, y):
    result = math.sqrt(abs(math.pow(x, 2) + math.pow(y, 2)))
    return result


first_hypotenuse = hypotenuse(first_x, first_y)
second_hypotenuse = hypotenuse(second_x, second_y)

if first_hypotenuse <= second_hypotenuse:
    print(f"({int(first_x)}, {int(first_y)})")
else:
    print(f"({int(second_x)}, {int(second_y)})")
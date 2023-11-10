numbers = [int(x) for x in input().split(", ")]

positive = ', '.join([str(x) for x in numbers if x >= 0])
negative = ', '.join([str(x) for x in numbers if x < 0])
even = ', '.join([str(x) for x in numbers if x % 2 == 0])
odd = ', '.join([str(x) for x in numbers if x % 2 != 0])

print(f"Positive: {positive}\n"
      f"Negative: {negative}\n"
      f"Even: {even}\n"
      f"Odd: {odd}\n")

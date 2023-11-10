
numbers_list = [int(input()), int(input()), int(input())]
negative_count = 0

for number in numbers_list:
    if number < 0:
        negative_count += 1

if 0 in numbers_list:
    result = "zero"
elif negative_count == 0 or negative_count == 2:
    result = "positive"
else:
    result = "negative"

print(result)

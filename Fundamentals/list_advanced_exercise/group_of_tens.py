numbers = [int(x) for x in input().split(", ")]
group_number = 10

while len(numbers) > 0:
    group = []
    copy = numbers.copy()
    for number in copy:
        if number <= group_number:
            group.append(number)
            numbers.pop(numbers.index(number))
    print(f"Group of {group_number}'s: {group}")
    group_number += 10



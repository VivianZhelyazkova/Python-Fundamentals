list_of_numbers = [int(x) for x in input().split()]

average = sum(list_of_numbers) / len(list_of_numbers)
greater_nums = list(filter(lambda x: x > average, list_of_numbers))
sorted_nums = sorted(greater_nums, reverse=True)
sorted_as_string = [str(x) for x in sorted_nums]
if not greater_nums:
    print("No")
print(" ".join(sorted_as_string[:min(len(sorted_as_string), 5)]))

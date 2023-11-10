my_list = [int(x) for x in input().split(", ")]

unique_numbers = list(filter(lambda x: my_list.count(x) == 1,my_list))

print(len(unique_numbers))


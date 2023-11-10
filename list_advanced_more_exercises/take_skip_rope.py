string = list(input())
list_of_chars = [x for x in string if not x.isnumeric()]
list_of_numbers = list(filter(lambda x: x.isnumeric(), string))

take_list = []
skip_list = []

for num in range(len(list_of_numbers)):
    if num % 2 == 0:
        take_list.append(int(list_of_numbers[num]))
    else:
        skip_list.append(int(list_of_numbers[num]))

result = []

for i in range(len(take_list)):
    take = take_list[i]
    skip = skip_list[i]
    result += list_of_chars[: take]
    list_of_chars = list_of_chars[take + skip:]

print("".join(result))


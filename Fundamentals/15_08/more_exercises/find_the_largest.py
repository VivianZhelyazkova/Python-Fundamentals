number = input()

my_list = list(number)
sorted_list = sorted(my_list, reverse=True)
result = ''.join(sorted_list)

print(str(result))
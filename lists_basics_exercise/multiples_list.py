factor = int(input())
count = int(input())
my_list = []

for n in range(count):
    current_number = (n + 1) * factor
    my_list.append(current_number)
print(my_list)
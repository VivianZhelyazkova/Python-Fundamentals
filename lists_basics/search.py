lines = int(input())
keyword = input()
my_list = []
filtered_list = []

for line in range(lines):
    current_string = input()
    my_list.append(current_string)
    if keyword in current_string:
        filtered_list.append(current_string)

print(my_list)
print(filtered_list)
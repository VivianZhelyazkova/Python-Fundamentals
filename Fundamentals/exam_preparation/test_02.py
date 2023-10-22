test_list1 = [[1, 2], [3, 4], [5, 6]]
test_list2 = [[3, 4], [5, 7], [1, 2]]

unique_element = []

for num in test_list1:
    if num not in test_list2:
        unique_element.append(num)
for num in test_list2:
    if num not in test_list1:
        unique_element.append(num)

print(unique_element)

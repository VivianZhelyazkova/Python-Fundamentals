sequence = input().split()
my_dict = {}

for element in sequence:
    lower_case_element = element.lower()
    if lower_case_element not in my_dict.keys():
        my_dict[lower_case_element] = 1
    else:
        my_dict[lower_case_element] += 1

odd_occurrences = {key: value for key, value in my_dict.items() if value % 2 != 0}
sorted_occurrences = dict(sorted(odd_occurrences.items(), key=lambda item: item[1], reverse=True))

keys = " ".join(odd_occurrences.keys())
print(keys)

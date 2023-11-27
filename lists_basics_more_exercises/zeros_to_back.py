list_of_numbers = input().split(', ')

for number in list_of_numbers:
    if number == "0":
        list_of_numbers.remove(number)
        list_of_numbers.append(number)
list_of_integers = [int(x) for x in list_of_numbers]

print(list_of_integers)

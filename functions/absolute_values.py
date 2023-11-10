# list_of_numbers = [abs(float(i)) for i in input().split(" ")]
# print(list_of_numbers)

list_of_numbers = input().split(" ")


def absolute(my_list):
    absolute_list = []
    for number in my_list:
        number = float(number)
        absolute_number = abs(number)
        absolute_list.append(absolute_number)
    return absolute_list


print(absolute(list_of_numbers))


string = input()
my_list = string.split(' ')
# new_list = list(map(lambda x: int(x) * -1, my_list))


def my_map(my_lambda, lista):
    result_list = []
    for i in lista:
        element = my_lambda(i)
        result_list.append(element)
    return result_list


new_list = my_map(lambda x: int(x) * -1, my_list)
print(new_list)

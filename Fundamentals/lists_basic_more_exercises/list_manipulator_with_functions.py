my_list = [int(i) for i in input().split(" ")]


def exchange(ex_list, cmd):
    indx = int(cmd.split(" ")[1])

    if indx >= len(ex_list) or indx < 0:
        print("Invalid index")
        return ex_list
    else:
        first_half = ex_list[:indx + 1]
        second_half = ex_list[indx + 1:]
        return second_half + first_half


def max_min_even_odd(max_min_list, cmd):
    is_even = cmd.split(" ")[1] == "even"
    is_max = cmd.split(" ")[0] == "max"
    min_num = 1001
    max_num = 0
    result_index = -1
    for n in max_min_list:
        if is_max:
            min_max_check = n > max_num
        else:
            min_max_check = n < min_num
        if is_even:
            even_odd_check = n % 2 == 0
        else:
            even_odd_check = n % 2 != 0
        if min_max_check and even_odd_check:
            max_num = n
            min_num = n
    for indx in range(len(max_min_list) - 1, -1, -1):
        if ((max_min_list[indx] == max_num and is_max)
                or (max_min_list[indx] == min_num and not is_max)):
            result_index = indx
            break
        elif max_min_list[indx] == min_num and not is_max:
            result_index = indx
            break
    if result_index > -1:
        print(result_index)
    else:
        print("No matches")


def first_last(first_last_list,cmd):
    part, count, even_or_odd = cmd.split(" ")
    count = int(count)
    is_even = even_or_odd == "even"
    even_odd_list = []
    if count > len(first_last_list):
        print("Invalid count")
    else:
        if part == "first":
            for digit in first_last_list:
                if is_even:
                    even_odd_check = digit % 2 == 0
                else:
                    even_odd_check = digit % 2 != 0
                if len(even_odd_list) == count:
                    break
                if even_odd_check:
                    even_odd_list.append(digit)
        else:
            for indx in range(len(first_last_list) - 1, -1, -1):
                if len(even_odd_list) == count:
                    break
                if is_even:
                    even_odd_check = first_last_list[indx] % 2 == 0
                else:
                    even_odd_check = first_last_list[indx] % 2 != 0
                if even_odd_check:
                    even_odd_list.append(first_last_list[indx])
            even_odd_list.reverse()
        print(even_odd_list)


while True:
    command = input()
    if command.split()[0] == "end":
        break
    if "exchange" in command:
        my_list = exchange(my_list, command)

    elif "max" in command or "min" in command:
        max_min_even_odd(my_list, command)

    elif "first" in command:
        first_last(my_list, command)

    elif "last" in command:
        first_last(my_list, command)

print(my_list)












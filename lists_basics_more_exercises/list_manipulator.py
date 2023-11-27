my_list = [int(i) for i in input().split(" ")]


while True:
    command = input()
    if command.split()[0] == "end":
        break
    if "exchange" in command:
        index = int(command.split(" ")[1])

        if index >= len(my_list) or index < 0:
            print("Invalid index")
        else:
            first_half = my_list[:index + 1]
            second_half = my_list[index + 1:]
            my_list = second_half + first_half
    elif "max" in command:
        max_num = 0
        max_index = -1
        even_or_odd = command.split(" ")[1]
        if even_or_odd == "even":
            for n in my_list:
                if n > max_num and n % 2 == 0:
                    max_num = n
            for index in range(len(my_list) - 1, -1, -1):
                if my_list[index] == max_num:
                    max_index = index
                    break
            if max_index > -1:
                print(max_index)
            else:
                print("No matches")

        if even_or_odd == "odd":
            for n in my_list:
                if n > max_num and n % 2 != 0:
                    max_num = n
            for index in range(len(my_list) - 1, -1, -1):
                if my_list[index] == max_num:
                    max_index = index
                    break
            if max_index > -1:
                print(max_index)
            else:
                print("No matches")
    elif "min" in command:
        min_num = 1001
        min_index = -1
        even_or_odd = command.split(" ")[1]
        if even_or_odd == "even":
            for n in my_list:
                if n < min_num and n % 2 == 0:
                    min_num = n
            for index in range(len(my_list) - 1, -1, -1):
                if my_list[index] == min_num:
                    min_index = index
                    break
            if min_index > -1:
                print(min_index)
            else:
                print("No matches")
        if even_or_odd == "odd":
            for n in my_list:
                if n < min_num and n % 2 != 0:
                    min_num = n
            for index in range(len(my_list) - 1, -1, -1):
                if my_list[index] == min_num:
                    min_index = index
                    break
            if min_index > -1:
                print(min_index)
            else:
                print("No matches")
    elif "first" in command:
        part, count, even_or_odd = command.split(" ")
        count = int(count)
        if even_or_odd == "even":
            even_list = []
            if count > len(my_list):
                print("Invalid count")
            else:
                for digit in my_list:
                    if len(even_list) == count:
                        break
                    if digit % 2 == 0:
                        even_list.append(digit)
                print(even_list)
        elif even_or_odd == "odd":
            odd_list = []
            if count > len(my_list):
                print("Invalid count")
            else:
                for digit in my_list:
                    if len(odd_list) == count:
                        break
                    if digit % 2 != 0:
                        odd_list.append(digit)
                print(odd_list)
    elif "last" in command:
        part, count, even_or_odd = command.split(" ")
        count = int(count)
        if even_or_odd == "even":
            even_list = []
            if count > len(my_list):
                print("Invalid count")
            else:
                for index in range(len(my_list) - 1, -1, -1):
                    if len(even_list) == count:
                        break
                    if my_list[index] % 2 == 0:
                        even_list.append(my_list[index])
                even_list.reverse()
                print(even_list)
        elif even_or_odd == "odd":
            odd_list = []
            if count > len(my_list):
                print("Invalid count")
            else:
                for index in range(len(my_list) - 1, -1, -1):
                    if len(odd_list) == count:
                        break
                    if my_list[index] % 2 != 0:
                        odd_list.append(my_list[index])
                odd_list.reverse()
                print(odd_list)

print(my_list)












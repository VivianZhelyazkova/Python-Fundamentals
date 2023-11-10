first_number = int(input())
second_number = int(input())
third_number = int(input())


def find_smallest(first, second, third):
    # smallest = first
    # if second < first:
    #     smallest = second
    # if third < smallest:
    #     smallest = third
    # return smallest
    my_numbers = [first, second, third]
    smallest = first
    for n in my_numbers:
        if n < smallest:
            smallest = n
    return smallest


print(find_smallest(first_number,second_number,third_number))
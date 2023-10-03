numbers = [int(i) for i in input().split(" ")]


# def is_even(x):
#     return x % 2 == 0


even_list = list(filter(lambda x: x % 2 == 0, numbers))

print(even_list)

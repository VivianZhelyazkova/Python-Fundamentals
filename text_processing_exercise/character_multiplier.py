strings = input().split()

first = strings[0]
second = strings[1]

total_sum = 0

len_first = len(first)
len_second = len(second)

if len_first > len_second:
    for index in range(len_second):
        total_sum += ord(first[index]) * ord(second[index])

    for i in range(len_second, len_first):
        total_sum += ord(first[i])
else:
    for index in range(len_first):
        total_sum += ord(first[index]) * ord(second[index])
    for i in range(len_first, len_second):
        total_sum += ord(second[i])

print(total_sum)

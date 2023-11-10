sequence_of_numbers = input().split(" ")
string = [*input()]
list_of_sums = []
message = []

for n in sequence_of_numbers:
    list_of_digits = []
    for digit in n:
        list_of_digits.append(int(digit))
    list_of_sums.append(sum(list_of_digits))

for s in list_of_sums:
    if s >= len(string):
        s = s - len(string)
    for i in range(len(string)):
        if s == i:
            message.append(string[i])
            string.pop(i)

print("".join(message))




first_string = input()
second_string = input()

for i in range(len(second_string)):
    if first_string[i] == second_string[i]:
        continue
    first_part = second_string[0:i+1]
    second_part = first_string[i+1: len(second_string)]
    result = first_part + second_part
    print(result)
string = input()

result = string[0]

for i in range(1,len(string)):

    if string[i] != string[i - 1]:
        result += string[i]

print(result)

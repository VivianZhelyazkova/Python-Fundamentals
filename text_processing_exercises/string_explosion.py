string = input()

result = ""
explosion = 0
lenght = 0

while lenght < len(string):
    for i in range(len(string)):
        if not string[i] == ">" and explosion > 0:
            explosion -= 1
        elif string[i] == ">":
            explosion += int(string[i + 1])
            result += string[i]
        else:
            result += string[i]
        lenght += 1
print(result)

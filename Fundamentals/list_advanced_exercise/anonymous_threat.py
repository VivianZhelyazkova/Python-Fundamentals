strings = input().split()
command = input()


while command != "3:1":
    merged = ""
    if "merge" in command:
        cmd, startindx, endindx = command.split()
        start = int(startindx)
        end = int(endindx)
        if start < 0:
            start = 0
        if end > (len(strings) - 1):
            end = len(strings) - 1
        for i in range(start, end + 1):
            merged += strings[i]
        first_part = strings[:start]
        second_part = strings[end + 1:]
        strings = first_part + [merged] + second_part
    if "divide" in command:
        cmd, index, partitions = command.split()
        index = int(index)
        partitions = int(partitions)
        current_string = strings[index]
        substring_length = len(current_string) // partitions
        remainder = len(current_string) % partitions
        substrings = []
        for i in range(partitions):
            start = i * substring_length
            end = (i + 1) * substring_length
            if i == partitions - 1:
                end += remainder
            substring = current_string[start:end]
            substrings.append(substring)
        first_part = strings[:index]
        second_part = strings[index + 1:]
        strings.pop(index)
        strings = first_part + substrings + second_part
    command = input()

print(" ".join(strings))


number = int(input())

for string in range(number):
    current_string = input()
    if "_" in current_string or "," in current_string or "." in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")

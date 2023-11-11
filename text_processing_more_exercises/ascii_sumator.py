first_symbol = input()
second_symbol = input()
start = ord(first_symbol)
final = ord(second_symbol)
string = input()

result = 0

for char in string:
    if ord(char) in range(start +1 ,final):
        result += ord(char)
print(result)
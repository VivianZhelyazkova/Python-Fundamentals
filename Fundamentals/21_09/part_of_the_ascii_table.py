start_index = int(input())
final_index = int(input())
result = ""
for i in range(start_index, final_index + 1):
    result += chr(i) + " "
print(result.rstrip())
    
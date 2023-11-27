list_of_numbers = input().split()
k = int(input())
dead_people = []
current_index = 0

while len(list_of_numbers) > 0:
    current_index += k - 1
    while current_index >= len(list_of_numbers):
        current_index = current_index - len(list_of_numbers)
    dead_people.append(list_of_numbers.pop(current_index))


print("[" + ",".join(dead_people) + "]")
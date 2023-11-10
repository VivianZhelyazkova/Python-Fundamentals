string_with_coma = input()
count_of_beggars = int(input())

list_of_numbers = string_with_coma.split(', ')
list_of_sums = [0] * count_of_beggars
current_beggar_index = 0

while True:
    if len(list_of_numbers) == 0:
        break
    if current_beggar_index == count_of_beggars:
        current_beggar_index = 0
    first_pile = int(list_of_numbers.pop(0))
    list_of_sums[current_beggar_index] += first_pile
    current_beggar_index += 1

print(list_of_sums)

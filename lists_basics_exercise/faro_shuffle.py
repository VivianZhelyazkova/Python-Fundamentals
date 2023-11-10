string = input()
count_of_shuffles = int(input())

list_of_cards = string.split(' ')

for j in range(count_of_shuffles):
    new_list = []
    first_half = list_of_cards[:len(list_of_cards) // 2]
    second_half = list_of_cards[len(list_of_cards) // 2:]

    for i in range(len(list_of_cards)):
        if i % 2 == 0:
            new_list.append(first_half.pop(0))
        else:
            new_list.append(second_half.pop(0))

    list_of_cards = new_list

print(new_list)

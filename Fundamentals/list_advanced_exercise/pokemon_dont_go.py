distances = [int(x) for x in input().split()]
removed_elements = []

while len(distances) > 0:
    index = int(input())
    value_of_pokemon = 0
    if index < 0:
        value_of_pokemon = distances.pop(0)
        last_element = distances[-1]
        distances.insert(0, last_element)
    elif index > len(distances) - 1:
        value_of_pokemon = distances.pop()
        distances.append(distances[0])
    else:
        value_of_pokemon = distances.pop(index)
    for i in range(len(distances)):
        if distances[i] <= value_of_pokemon:
            distances[i] += value_of_pokemon
        else:
            distances[i] -= value_of_pokemon

    removed_elements.append(value_of_pokemon)

print(sum(removed_elements))

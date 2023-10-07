elements = input().split()
command = input()
moves = 0

while command != "end":
    first_index, second_index = command.split()
    moves += 1
    first_index = int(first_index)
    second_index = int(second_index)
    if first_index == second_index \
            or first_index not in range(len(elements)) \
            or second_index not in range(len(elements)):
        midpoint = (len(elements) // 2)
        additional_element = "-" + str(moves) + "a"
        elements = elements[:midpoint] + [additional_element] + [additional_element] + elements[midpoint:]
        print("Invalid input! Adding additional elements to the board")
    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        element = elements[first_index]
        elements.remove(element)
        elements.remove(element)
    elif elements[first_index] != elements[second_index]:
        print("Try again!")
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
    command = input()

if command == "end" and len(elements) > 0:
    print(f"Sorry you lose :(\n"
          f"{' '.join(elements)}")

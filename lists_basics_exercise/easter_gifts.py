gifts = input()
list_of_gifts = gifts.split(' ')
command = input()

while command != 'No Money':
    if 'OutOfStock' in command:
        action, value = command.split(' ')
        for i in range(len(list_of_gifts)):
            if value == list_of_gifts[i]:
                list_of_gifts[i] = 'None'
    elif "Required" in command:
        action, value, index = command.split(' ')
        # value = command.split(' ')[1]
        # index = command.split(' ')[2]
        index = int(index)
        for i in range(len(list_of_gifts)):
            if index == i:
                list_of_gifts[i] = value
    elif "JustInCase" in command:
        action,value = command.split(' ')
        # value = command.split(" ")[1]
        list_of_gifts.pop()
        list_of_gifts.append(value)
    command = input()

list_of_gifts = [gift for gift in list_of_gifts if gift != 'None']
print(" ".join(list_of_gifts))

line = input()

my_list = line.split(', ')
if my_list[len(my_list)-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(my_list)):
        if my_list[i] == "wolf":
            print(f"Oi! Sheep number {len(my_list) - i - 1}! You are about to be eaten by a wolf!")



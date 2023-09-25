word = input()
my_list = []

for i in range(len(word)):
    if word[i].isupper():
        my_list.append(i)
print(my_list)
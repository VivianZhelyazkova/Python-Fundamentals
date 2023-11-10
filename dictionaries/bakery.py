items = input().split()
bakery = {}

for index in range(0, len(items), 2):
    key = items[index]
    value = int(items[index + 1])
    bakery[key] = value

print(bakery)

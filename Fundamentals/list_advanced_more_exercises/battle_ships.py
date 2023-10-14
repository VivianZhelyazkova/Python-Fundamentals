rows = int(input())
battlefield = []
for row in range(rows):
    ships_health = [int(x) for x in input().split()]
    battlefield.append(ships_health)
attacks = input().split()
ships_wrecked = 0
for i in range(len(attacks)):
    row, column = attacks[i].split("-")
    row = int(row)
    column = int(column)
    if battlefield[row][column] > 0:
        battlefield[row][column] -= 1
        if battlefield[row][column] == 0:
            ships_wrecked += 1
print(ships_wrecked)



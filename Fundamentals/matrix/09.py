x = 5
y = 4
matrix = []
number = 1
for column in range(y):
    rows = []
    for row in range(x):
        rows.append(0)
    matrix.append(rows)

number = 1

for horizontal in range(x):
    for vertical in range(y):
        matrix[vertical][horizontal] = number
        number += 1

for row in matrix:
    print(row)
    
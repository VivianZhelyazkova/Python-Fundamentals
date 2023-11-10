rows = int(input())
matrix = []
for i in range(rows):
    row = input().split()
    matrix.append(row)
print(matrix)

dots_counter = 0

def connect(x, y):
    
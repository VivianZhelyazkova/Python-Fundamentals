electrons = int(input())
n = 0
shells = []

while electrons > 0:
    n += 1
    max_shell_capacity = 2 * n ** 2
    if electrons >= max_shell_capacity:
        electrons -= max_shell_capacity
        shells.append(max_shell_capacity)
    else:
        shells.append(electrons)
        break

print(shells)


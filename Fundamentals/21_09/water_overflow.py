lines = int(input())
capacity = 255
total_liters = 0


for i in range(lines):
    liters = int(input())
    if liters <= capacity:
        capacity -= liters
        total_liters += liters
    else:
        print(f"Insufficient capacity!")

print(total_liters)

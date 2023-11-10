cells_with_fire = input()
water = int(input())

HIGH_RANGE = range(81, 125 + 1)
MEDIUM_RANGE = range(51, 80 + 1)
LOW_RANGE = range(1, 50 + 1)
effort = 0
total_fire = 0
valid_cells_list = []

list_of_cells = cells_with_fire.split('#')

for cell in list_of_cells:
    fire_type, cell_value = cell.split(' = ')
    cell_value = int(cell_value)
    if water == 0:
        break
    if fire_type == 'High':
        if cell_value not in HIGH_RANGE:
            continue
    elif fire_type == 'Medium':
        if cell_value not in MEDIUM_RANGE:
            continue
    elif fire_type == 'Low':
        if cell_value not in LOW_RANGE:
            continue
    if water >= cell_value:
        water -= cell_value
        effort += cell_value * 0.25
        total_fire += cell_value
        valid_cells_list.append(cell_value)
print("Cells:")
for cell in valid_cells_list:
    print(f" - {cell}")

print(f"Effort: {effort:.2f}\n"
      f"Total Fire: {total_fire}")
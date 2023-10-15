pirate_ship_status = [int(x) for x in input().split(">")]
warship_status = [int(x) for x in input().split(">")]
max_section_health = int(input())
command = input()
is_stalemate = True

while command != "Retire":
    if "Fire" in command:
        cmd, index, damage = command.split()
        index = int(index)
        damage = int(damage)
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_stalemate = False
                break
    elif "Defend" in command:
        cmd, start_index, end_index, damage = command.split()
        start_index = int(start_index)
        end_index = int(end_index)
        damage = int(damage)
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            for index in range(start_index, end_index + 1):
                pirate_ship_status[index] -= damage
                if pirate_ship_status[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_stalemate = False
                    break
    elif "Repair" in command:
        cmd, index, health = command.split()
        index = int(index)
        health = int(health)
        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_section_health:
                pirate_ship_status[index] = max_section_health
    elif "Status" in command:
        broken_sections = 0
        need_repair = max_section_health * 0.20
        for section in pirate_ship_status:
            if section < need_repair:
                broken_sections += 1
        print(f"{broken_sections} sections need repair.")
    command = input()


if is_stalemate:
    print(f"Pirate ship status: {sum(pirate_ship_status)}\n"
          f"Warship status: {sum(warship_status)}")



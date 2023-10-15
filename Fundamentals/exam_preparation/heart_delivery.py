neighborhood_houses = [int(x) for x in input().split("@")]
command = input()
current_jump = 0

while command != "Love!":
    cmd, jump = command.split()
    jump = int(jump)
    current_jump += jump
    if current_jump >= len(neighborhood_houses):
        current_jump = 0
    if neighborhood_houses[current_jump] > 0:
        neighborhood_houses[current_jump] -= 2
        if neighborhood_houses[current_jump] == 0:
            print(f"Place {current_jump} has Valentine's day.")
    else:
        print(f"Place {current_jump} already had Valentine's day.")
    command = input()
print(f"Cupid's last position was {current_jump}.")

failed_houses = list(filter(lambda x: x != 0, neighborhood_houses))

if len(failed_houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(failed_houses)} places.")

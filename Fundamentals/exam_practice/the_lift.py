people_count = int(input())
lift_state = [int(x) for x in input().split()]

wagon_max_capacity = 4
has_empty_space = False
for wagon in range(len(lift_state)):
    available_seats = wagon_max_capacity - lift_state[wagon]
    people_lifted = 0
    if people_count >= available_seats:
        people_count -= available_seats
        people_lifted = available_seats
    else:
        people_lifted = people_count
        people_count = 0
        has_empty_space = True
    lift_state[wagon] += people_lifted

if people_count > 0:
    print(f"There isn't enough space! {people_count} people in a queue!")
if has_empty_space:
    print("The lift has empty spots!")
print(*lift_state, sep=" ")

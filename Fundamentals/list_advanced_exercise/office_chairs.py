number_of_rooms = int(input())
room_counter = 0
free_chairs = 0
is_busy = False

for room in range(1, number_of_rooms + 1):
    room_counter += 1
    information = input()
    chairs, visitors = information.split()
    visitors = int(visitors)
    if len(chairs) < visitors:
        print(f"{visitors - len(chairs)} more chairs needed in room {room_counter}")
        is_busy = True
    else:
        free_chairs += len(chairs) - visitors

if not is_busy:
    print(f"Game On, {free_chairs} free chairs left")

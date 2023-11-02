number_of_commands = int(input())
system = {}
for command in range(number_of_commands):
    action = input().split()
    action_type = action[0]
    username = action[1]
    if "unregister" == action[0]:
        if username not in system:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            system.pop(username)
    elif "register" == action[0]:
        license_plate_number = action[2]
        if username not in system:
            system[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

for user, plate in system.items():
    print(f"{user} => {plate}")

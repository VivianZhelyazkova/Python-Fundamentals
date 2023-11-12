keys = [int(x) for x in input().split()]
command = input()

treasure = ""
coordinates = ""

while command != "find":
    key_index = 0
    decrypted_message = ""
    for char in command:
        new_char = chr(ord(char) - keys[key_index])
        decrypted_message += new_char
        key_index = (key_index + 1) % len(keys)
    treasure = ""
    coordinates = ""
    treasure_found = False
    coordinates_found = False
    for char in decrypted_message:
        if treasure_found and char != "&":
            treasure += char
        if char == "&":
            treasure_found = not treasure_found
        if coordinates_found and char != ">":
            coordinates += char
        if char == "<":
            coordinates_found = True

    print(f"Found {treasure} at {coordinates}")
    command = input()

number = int(input())
pieces = {}
for line in range(number):
    command = input()
    piece, composer, key = command.split("|")
    pieces[piece] = [composer, key]

command = input()

while command != "Stop":
    if "Add" in command:
        cmd, piece, composer, key = command.split("|")
        if piece not in pieces:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif "Remove" in command:
        cmd, piece = command.split("|")
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif "ChangeKey" in command:
        cmd, piece, new_key = command.split("|")
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}")

sequence = input().split()
repeated_sequence = ""

for string in sequence:

    repeated_sequence += string * len(string)

print(repeated_sequence)
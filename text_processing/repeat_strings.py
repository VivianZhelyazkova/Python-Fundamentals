sequence = input().split()
# repeated_sequence = ""
#
# for string in sequence:
#
#     repeated_sequence += string * len(string)

repeated_sequence = "".join([string * len(string) for string in sequence])

print(repeated_sequence)

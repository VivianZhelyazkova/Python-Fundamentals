old_version = [int(x) for x in input().split(".")]

old_version[2] += 1
if old_version[2] == 10:
    old_version[2] = 0
    old_version[1] += 1
    if old_version[1] == 10:
        old_version[1] = 0
        old_version[0] += 1

new_version = map(lambda x: str(x), old_version)

print(".".join(new_version))

# print(".".join(list(str(int("".join(input().split("."))) + 1))))

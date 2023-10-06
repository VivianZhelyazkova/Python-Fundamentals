targets = input().split()
command = input()
shot_targets = 0

while command != "End":
    index = int(command)
    if index not in range(len(targets)):
        command = input()
        continue
    for i in range(len(targets) + 1):
        if i == index:
            if targets[i] != "-1":
                shot_targets += 1
                target_health = targets[i]
                targets[i] = "-1"
                for target in targets:
                    target_int = int(target)
                    if i != targets.index(target):
                        if target != "-1":
                            if target_int > int(target_health):
                                target_int -= int(target_health)
                                targets[targets.index(target)] = str(target_int)
                            else:
                                target_int += int(target_health)
                                targets[targets.index(target)] = str(target_int)

    command = input()

if command == "End":
    print(f"Shot targets: {shot_targets} -> {' '.join(targets)}")

targets = [int(x) for x in input().split()]
command = input()

while "End" not in command:
    index_to_shoot = int(command)
    if 0 <= index_to_shoot < len(targets):
        if targets[index_to_shoot] >= 0:
            for i in range(0, len(targets)):
                if i != index_to_shoot and targets[i] >= 0:
                    if targets[i] > targets[index_to_shoot]:
                        targets[i] -= targets[index_to_shoot]
                    else:
                        targets[i] += targets[index_to_shoot]
            targets[index_to_shoot] = -1
    command = input()

shot_targets = len(list(filter(lambda x: x == -1, targets)))
print(f"Shot targets: {shot_targets} -> {' '.join([str(x) for x in targets])}")
# 90/100
# targets = input().split()
# command = input()
# shot_targets = 0
#
# while command != "End":
#     index = int(command)
#     if index not in range(len(targets)):
#         command = input()
#         continue
#     for i in range(len(targets) + 1):
#         if i == index:
#             if targets[i] != "-1":
#                 shot_targets += 1
#                 target_health = targets[i]
#                 targets[i] = "-1"
#                 for target in targets:
#                     target_int = int(target)
#                     if i != targets.index(target):
#                         if target != "-1":
#                             if target_int > int(target_health):
#                                 target_int -= int(target_health)
#                                 targets[targets.index(target)] = str(target_int)
#                             else:
#                                 target_int += int(target_health)
#                                 targets[targets.index(target)] = str(target_int)
#
#     command = input()
#
# if command == "End":
#     print(f"Shot targets: {shot_targets} -> {' '.join(targets)}")

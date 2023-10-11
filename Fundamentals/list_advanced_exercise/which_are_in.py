first_line = input().split(", ")
second_line = input().split(", ")
# new_list = []
# for line in first_line:
#     for word in second_line:
#         if line in word:
#             if line not in new_list:
#                 new_list.append(line)
#
# print(new_list)

filtered = list(filter(lambda x: [y for y in second_line if x in y], first_line))
print(filtered)

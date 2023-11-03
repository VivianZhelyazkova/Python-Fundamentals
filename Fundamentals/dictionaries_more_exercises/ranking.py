line = input()

contests = {}

while line != "end of contests":
    contest, password = line.split(":")
    contests[contest] = password
    line = input()

second_line = input()

submissions = {}
best_candidate = {}

while second_line != "end of submissions":
    contest, password, username, points = second_line.split("=>")
    points = int(points)

    if contest in contests:
        if contests[contest] == password:
            if username not in submissions:
                submissions[username] = {contest: points}
            else:
                if contest in submissions[username]:
                    if points > submissions[username][contest]:
                        submissions[username][contest] = points
                else:
                    submissions[username][contest] = points

    second_line = input()

best_candidate = []
max_points = 0
for username, contest in submissions.items():
    total_points_per_user = 0
    for key, value in contest.items():
        total_points_per_user += value
    if total_points_per_user > max_points:
        max_points = total_points_per_user
        best_candidate = [username, total_points_per_user]

print(f"Best candidate is {best_candidate[0]} with total {best_candidate[1]} points.")

sorted_names = dict(sorted(submissions.items()))

for username, contests in sorted_names.items():
    sorted_names[username] = dict(sorted(contests.items(), key=lambda item: item[1], reverse=True))
print("Ranking:")
for username,contests in sorted_names.items():
    print(f"{username}")
    for contest,points in contests.items():
        print(f"#  {contest} -> {points}")

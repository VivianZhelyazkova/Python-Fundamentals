line = input()

contests = {}

while line != "no more time":
    username, contest, points = line.split(" -> ")
    points = int(points)
    if contest not in contests:
        contests[contest] = {username: points}
    elif username not in contests[contest]:
        contests[contest][username] = points
    elif points > contests[contest][username]:
        contests[contest][username] = points
    line = input()

for contest, info in contests.items():
    print(f"{contest}: {len(info)} participants")
    sorted_by_points = dict(sorted(info.items(), key=lambda x: (-x[1], x[0])))
    for rank, (name, points) in enumerate(sorted_by_points.items(), start=1):
        print(f"{rank}. {name} <::> {points}")

print("Individual standings:")

total_points = {}
for contest, info in contests.items():
    for username, points in info.items():
        if username in total_points:
            total_points[username] += points
        else:
            total_points[username] = points
sorted_by_points = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))
for rank, (username, points) in enumerate(sorted_by_points.items(), start=1):
    print(f"{rank}. {username} -> {points}")

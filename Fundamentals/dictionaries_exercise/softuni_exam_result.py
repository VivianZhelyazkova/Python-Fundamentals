command = input()

results = {}
submissions = {}

while command != "exam finished":

    if "banned" in command:
        name, action = command.split("-")
        del results[name]
        command = input()
        continue

    name, language, points = command.split("-")
    points = int(points)
    if name not in results:
        results[name] = points
    else:
        if points > results[name]:
            results[name] = points
    if language not in submissions:
        submissions[language] = 1
    else:
        submissions[language] += 1
    command = input()

print("Results:")
for name, points in results.items():
    print(f"{name} | {points}")
print("Submissions:")
for language, submission in submissions.items():
    print(f"{language} - {submission}")

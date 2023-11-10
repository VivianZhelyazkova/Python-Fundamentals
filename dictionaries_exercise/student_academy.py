pairs = int(input())
students = {}

for pair in range(pairs):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for student in students:
    students[student] = sum(students[student]) / len(students[student])

filtered_students = {student: avg for student, avg in students.items() if avg >= 4.50}

for name, grade in filtered_students.items():
    print(f"{name} -> {grade:.2f}")

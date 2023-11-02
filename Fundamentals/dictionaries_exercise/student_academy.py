pairs = int(input())
students = {}

for pair in range(pairs):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)
average_grades = {}
for student in students:
    average_grade = sum(students[student]) / len(students[student])
    average_grades[student] = average_grade
filtered_students = {student: avg for student, avg in average_grades.items() if avg >= 4.50}

for name, grade in filtered_students.items():
    print(f"{name} -> {grade:.2f}")

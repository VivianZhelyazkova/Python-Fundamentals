command = input()

students = {}

while ":" in command:
    name, student_id, course = command.split(":")
    student_id = int(student_id)
    course = "_".join(course.split())
    students[student_id] = [name, course]
    # students.update({student_id: [name, course]})
    command = input()

for student in students:
    if command == students[student][1]:
        print(f"{students[student][0]} - {student}")

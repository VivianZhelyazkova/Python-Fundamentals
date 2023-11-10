command = input()

register = {}

while command != "end":
    course, student = command.split(" : ")
    if course not in register:
        register[course] = []
    register[course].append(student)
    command = input()

for course, list_of_students in register.items():
    print(f"{course}: {len(list_of_students)}")
    for student in list_of_students:
        print(f"-- {student}")


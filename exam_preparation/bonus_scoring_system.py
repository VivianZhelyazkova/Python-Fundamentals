from math import ceil
number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendances = 0

for student in range(number_of_students):
    student_attendances = int(input())
    total_bonus = student_attendances / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendances = student_attendances
print(f"Max Bonus: {ceil(max_bonus)}.\n"
      f"The student has attended {max_attendances} lectures.")

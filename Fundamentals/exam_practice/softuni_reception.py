first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())
hour_count = 0

while students_count > 0:
    hour_count += 1
    if hour_count % 4 != 0:
        students_count -= first_employee_efficiency + second_employee_efficiency + third_employee_efficiency



print(f"Time needed: {hour_count}h.")


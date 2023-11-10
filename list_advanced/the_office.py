employees_happiness = [int(x) for x in input().split()]
improvement_factor = int(input())
after_improvement = list(map(lambda x: x * improvement_factor, employees_happiness))
average_happiness = sum(after_improvement) / len(employees_happiness)
happy_count = list(filter(lambda x: x >= average_happiness, after_improvement))

if len(happy_count) >= len(employees_happiness) // 2:
    print(f"Score: {len(happy_count)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{len(employees_happiness)}. Employees are not happy!")




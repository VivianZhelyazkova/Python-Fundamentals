line = input()

dict_of_companies = {}

while line != "End":
    company_name, employee_id = line.split(" -> ")
    if company_name not in dict_of_companies:
        dict_of_companies[company_name] = [employee_id]
    else:
        if employee_id not in dict_of_companies[company_name]:
            dict_of_companies[company_name].append(employee_id)

    line = input()

for company, employees in dict_of_companies.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
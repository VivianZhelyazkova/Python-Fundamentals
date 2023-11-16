import re

number = int(input())
regex = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
for line in range(number):
    barcode = input()
    match = re.findall(regex, barcode)
    if not match:
        print("Invalid barcode")
    else:
        if not bool(re.search(r'\d', barcode)):
            group = "00"
        else:
            group = ""
            for char in barcode:
                if char.isnumeric():
                    group += char
        print(f"Product group: {group}")

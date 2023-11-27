import re

number = int(input())

for line in range(number):
    barcode = input()
    regex = r"@#+[A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1}@#+"
    matches = re.findall(regex, barcode)
    if not matches:
        print("Invalid barcode")
    else:
        barcode = barcode.replace("@", "")
        barcode = barcode.replace("#", "")
        if barcode.isalpha():
            print("Product group: 00")
        else:
            product_group = "".join([symbol for symbol in barcode if symbol.isnumeric()])
            print(f"Product group: {product_group}")

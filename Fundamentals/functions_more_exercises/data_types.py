first_line = input()
second_line = input()


def data_type(f, s):
    if f == "int":
        result = int(s) * 2
    elif f == "real":
        result = f"{float(s) * 1.5:.2f}"
    elif f == "string":
        result = "$" + s + "$"
    return result


print(data_type(first_line, second_line))
number = int(input())


def loading(n):
    percents = (n // 10) * "%"
    if len(percents) < 10:
        blank = (10 - len(percents)) * "."
    else:
        blank = ""
    bar = percents + blank
    return bar


loading_bar = loading(number)

if number < 100:
    print(f"{number}% [{loading_bar}]")
    print("Still loading...")
elif number == 100:
    print("100% Complete!")
    print(f"[{loading_bar}]")
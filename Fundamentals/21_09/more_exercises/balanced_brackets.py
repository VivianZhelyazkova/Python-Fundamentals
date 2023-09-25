lines = int(input())
opened = False
closed = False
balanced = True
for line in range(lines):
    current_string = input()
    if current_string == "(":
        if opened:
            balanced = False
            break
        opened = True
    if current_string == ")":
        if opened:
            closed = True
            balanced = True
            opened = False
        else:
            balanced = False
            break

if balanced and closed:
    print("BALANCED")
else:
    print("UNBALANCED")

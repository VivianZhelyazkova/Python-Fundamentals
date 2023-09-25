budget = int(input())

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    budget -= int(command)
    if budget < 0:
        print("You went in overdraft!")
        break


number_of_cars = int(input())
obtained_cars = {}
for line in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    obtained_cars[car] = [int(mileage), int(fuel)]

command = input()

while command != "Stop":

    if "Drive" in command:
        cmd, car, distance, fuel = command.split(" : ")
        distance = int(distance)
        fuel = int(fuel)
        if obtained_cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            obtained_cars[car][1] -= fuel
            obtained_cars[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if obtained_cars[car][0] >= 100000:
                obtained_cars.pop(car)
                print(f"Time to sell the {car}!")
    elif "Refuel" in command:
        cdm, car, fuel = command.split(" : ")
        fuel = int(fuel)
        filled_liters = 75 - obtained_cars[car][1]
        obtained_cars[car][1] += fuel
        if obtained_cars[car][1] > 75:
            obtained_cars[car][1] = 75
            fuel = filled_liters
        print(f"{car} refueled with {fuel} liters")
    elif "Revert" in command:
        cmd, car, kilometers = command.split(" : ")
        kilometers = int(kilometers)
        obtained_cars[car][0] -= kilometers
        if obtained_cars[car][0] > 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        if obtained_cars[car][0] < 10000:
            obtained_cars[car][0] = 10000
    command = input()

for car, info in obtained_cars.items():
    print(f"{car} -> Mileage: {obtained_cars[car][0]} kms, Fuel in the tank: {obtained_cars[car][1]} lt.")

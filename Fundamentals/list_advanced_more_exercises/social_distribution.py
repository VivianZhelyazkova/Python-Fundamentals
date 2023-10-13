population = [int(x) for x in input().split(", ")]
min_wealth = int(input())

if sum(population) // len(population) < min_wealth:
    print("No equal distribution possible")
else:
    for index, person in enumerate(population):
        copy = population.copy()
        richest = max(population)
        richest_index = population.index(richest)
        if person < min_wealth:
            population[richest_index] -= min_wealth - person
            population[index] = min_wealth
            is_enough = True
    print(population)
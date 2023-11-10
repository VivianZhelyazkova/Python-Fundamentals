class Zoo:

    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self,species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self,species):
        names = []
        species_name = ""
        if species == "mammal":
            names = self.mammals
            species_name = "Mammals"
        elif species == "fish":
            names = self.fishes
            species_name = "Fishes"
        elif species == "bird":
            names = self.birds
            species_name = "Birds"
        return (f"{species_name} in {self.zoo_name}: {', '.join(names)}\n"
                f"Total animals: {Zoo.__animals}")


zoo_name = input()
number = int(input())
zoo = Zoo(zoo_name)

for n in range(number):
    species, name = input().split()
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))

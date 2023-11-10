class Circle:

    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        result = Circle.__pi * self.diameter
        return result

    def calculate_area(self):
        radius = self.diameter / 2
        result = Circle.__pi * radius ** 2
        return result

    def calculate_area_of_sector(self, angle):
        radius = self.diameter / 2
        result = angle/360 * Circle.__pi * radius ** 2
        return result



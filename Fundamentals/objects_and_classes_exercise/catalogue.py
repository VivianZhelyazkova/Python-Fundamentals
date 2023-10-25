class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, name: str):
        self.products.append(name)

    def get_by_letter(self, first_letter: str):
        filtered_list = list(filter(lambda x: x.startswith(first_letter), self.products))
        return filtered_list

    def __repr__(self):
        sorted_products = self.products.copy()
        sorted_products.sort()
        new_line = '\n'
        return (f"Items in the {self.name} catalogue:\n"
                f"{new_line.join(sorted_products)}")



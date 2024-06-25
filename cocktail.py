from ingredient import Ingredient


class Cocktail:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f'{self.name}: {self.ingredients}'

    def __repr__(self):
        return self.__str__()


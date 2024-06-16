from ingredient import Ingredient


class Cocktail:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def info(self):
        print(f'Cocktail {self.name}:')
        print(f'Ingridients: {[ing.info() for ing in self.ingredients]}')


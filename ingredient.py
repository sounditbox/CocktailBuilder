class Ingredient:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def info(self):
        return f'{self.name}, {self.size} ml'

#
# jag = Ingredient('Jagermeister', 50)
# print(jag.info())

from cocktail import Cocktail
from ingredient import Ingredient

jag = Ingredient('Jagermeister', 30)
rb = Ingredient('Red Bull', 120)

jager_bomb = Cocktail('Jager Bomb', [jag, rb])
jager_bomb.info()

print()

white_russian = Cocktail('White Russian', [
    Ingredient('Absolut', 60),
    Ingredient('Kahlua', 30),
    Ingredient('Prostokvashino Cream', 30)
])
white_russian.info()

B52 = Cocktail("B-52",[
    Ingredient("Baileys", 20),
    Ingredient("Cuantro", 20),
    Ingredient("Kahlua", 20)
]  )
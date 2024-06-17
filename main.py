from cocktail import Cocktail
from ingredient import Ingredient

jag = Ingredient('Jagermeister', 30)
rb = Ingredient('Red Bull', 120)

jager_bomb = Cocktail('Jager Bomb', [
    Ingredient("jagermeister",50),
    Ingredient("Red bull",150)
])

white_russian = Cocktail('White Russian', [
    Ingredient('Mamont', 60),
    Ingredient('Kahlua', 30),
    Ingredient('Prostokvashino Cream', 30)
])

B52 = Cocktail("B-52",[
    Ingredient("Baileys", 20),
    Ingredient("Cuantro", 20),
    Ingredient("Kahlua", 20)
])

pin = Cocktail("Pinakolada",[
    Ingredient("Bacardi black", 50),
    Ingredient("Planto", 50),
    Ingredient("Dobriy", 100)
])

Moj = Cocktail("Mojito",[
    Ingredient("Bacardi gold", 50),
    Ingredient("schweppes", 150),
    Ingredient("sugar syrope", 10),
    Ingredient("mint juice", 5)
])

niger = Cocktail("Negroni",[
    Ingredient("Bombay saphire", 30),
    Ingredient("Campari", 30),
    Ingredient("Martini fiero", 30)
])

her = Cocktail("Hirosima",[
    Ingredient("Cuantro", 20),
    Ingredient("baileys", 20),
    Ingredient("Xenta", 10),
    Ingredient("grenadine", 5)
])

Otv = Cocktail("Otvertka", [
    Ingredient("Mamont", 50),
    Ingredient("rich", 100)
])

old = Cocktail("Old faschion", [
    Ingredient("VSOP Remy Martin", 45),
    Ingredient("bitter Angosture", 4),
    Ingredient("Sugar syrope", 10)
])

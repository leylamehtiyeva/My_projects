"""NEED TO FINISH"""

"""RECIPE class to represent recipes.
The individual ingredients of a recipe must be defined by the class INGREDIENT"""

class Recipe:
    def __init__(self, *args):
        self.recipe = {'name': None, 'volume': None, 'measure': None}
        for key in self.recipe:
            for i in args:
                self.recipe[key] = args[i]
                continue


    def add_ingredient(self, ing):
        if ing.name not in self.recipe.name:
            self.recipe.append(ing)

    def remove_ingredient(self, ing):
        if ing.name in self.recipe.name:
            self.recipe.remove(ing)

    def get_ingredients(self):
        return tuple(self.recipe)

    def __len__(self):
        return len(self.get_ingredients())



class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure


    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"




recipe = Recipe()
i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")
recipe = Recipe(i1, i2, i3)
recipe.add_ingredient(i4)
recipe.remove_ingredient(i3)
n = len(recipe)
print(n)


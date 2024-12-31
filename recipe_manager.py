class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe_name):
        self.recipes = [recipe for recipe in self.recipes if recipe['name'] != recipe_name]

    def list_recipes(self):
        return self.recipes

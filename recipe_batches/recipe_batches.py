#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    def calc(key, value):
        try:
            return math.floor(ingredients[key] / value)
        except KeyError:
            return 0
    first_iteration = True
    max_batches = 0
    for key, value in recipe.items():
        if first_iteration:
            max_batches = calc(key, value)
            first_iteration = False
        else:
            working = calc(key, value)
            if working < max_batches:
                max_batches = working
    
    return max_batches



if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

# print(recipe_batches(
#     {'milk': 100, 'butter': 50, 'flour': 5},
#     {'milk': 200, 'butter': 100, 'flour': 51}
# ))

# DONE Iterate through each item in recipes
# DONE check if first iteration
    # DONE if it is
    # DONE max_batches = floor of division of first recipe item amount by first ingredients item amount 
    # DONE else
        # DONE divide current recipe item by ingredients item getting the largest whole number
        # DONE if that number is lower than current max_batches
    # DONE reassign max_batches to new lowest
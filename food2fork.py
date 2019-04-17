import requests
from pprint import pprint


def get_recipe(ingredient):

    api_key = '6057e26d2643268985352767e47fd9d1'
    #ingredient = 'chicken,tomato,'
    ingredient = input('What ingredients do you have? ')
    response = requests.get('https://www.food2fork.com/api/search?key={}&q={}'.format(api_key, ingredient))

    data = response.json()

    recipe = data

    return (recipe)


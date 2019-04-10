import requests
from pprint import pprint


def get_recipe(ingredient):
    api_key = '33aaefd0024a6798b6324f2670c67a4f'
    #api_key = '6057e26d2643268985352767e47fd9d1'
    #ingredient = 'chicken,tomato,'
    #ingredient = input('What ingredients do you have? ')
    response = requests.get('https://www.food2fork.com/api/search?key={}&q={}'.format(api_key, ingredient))

    data = response.json()
    #pprint(response.json())

    recipe = data

    #print(recipe['count'])
    #print(recipe['recipes'])
    #pprint(recipe['recipes'])
    return (recipe)


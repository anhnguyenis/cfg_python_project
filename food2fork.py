import requests
from pprint import pprint

api_key = '8d4b3dab2ea6f06e692d7cd775f149b7'
ingredient = 'avocado'

response = requests.get('https://www.food2fork.com/api/search?key={}&q={}'.format(api_key, ingredient))

pprint(response.json())


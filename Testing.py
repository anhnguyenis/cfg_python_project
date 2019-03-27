import requests
from pprint import pprint

url = 'https://api.kanye.rest'

response = requests.get(url)
quote = response.json()

print(quote)
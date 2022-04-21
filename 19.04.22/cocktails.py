import json
from urllib.request import urlopen

import requests

cocktail = 'margarita'
# description = urlopen(f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail}').read()
# print(json.loads(description)['drinks'][0]['strDrinkThumb'])
# image = urlopen(json.loads(description)['drinks'][0]['strDrinkThumb'])
# print(image)

description = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php', params={'s': cocktail})
# print(description.json()['drinks'][0]['strInstructions'])
image = requests.get(description.json()['drinks'][0]['strDrinkThumb'])
with open('margarita.jpg', 'wb') as file:
    file.write(image.content)

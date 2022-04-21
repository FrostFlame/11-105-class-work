'''amiibo'''
import os

# print(os.getcwd())
# print(os.listdir())
# os.makedirs('my_dir/1/2/3/4', exist_ok=True)
import requests

url = 'https://www.amiiboapi.com/api/amiibo/'

with open('names.txt', 'r', encoding='utf-8') as names:
    names = names.read().split()
    for name in names:
        response = requests.get(url, params={'character': name}).json()
        os.makedirs(response['amiibo'][0]['character'], exist_ok=True)
        for num, amiibo in enumerate(response['amiibo']):
            with open(f'{response["amiibo"][0]["character"]}/{response["amiibo"][0]["character"]}{num}.png', 'wb') as image:
                byte_image = requests.get(amiibo['image'])
                image.write(byte_image.content)
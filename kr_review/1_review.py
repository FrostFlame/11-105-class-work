import requests

n = int(input()) * 3

url = f'https://picsum.photos/v2/list'
response = requests.get(url, params={'limit': n})
print(response.json())

image = response.json()[0]['download_url']
response = requests.get(image)
with open('image.png', 'wb') as file:
    file.write(response.content)

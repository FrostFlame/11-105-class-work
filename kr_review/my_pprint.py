from pprint import pprint
import requests

response = requests.get('https://www.amiiboapi.com/api/amiibo/',
                        params={'character': 'link'}).json()

print(response)
pprint(response)
pprint({a: a for a in range(20)})

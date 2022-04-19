'''http://numverify.com'''
import json
from urllib.request import urlopen

import requests

# with urlopen('http://apilayer.net/api/validate?access_key=5d0e36b0ce7208b266d3b7ab51d01e90&number=+79655824681') as response:
#     print(response)
#     response = response.read().decode('utf-8')
#     print(response)
#     response = json.loads(response)
#     print(response['number'])


response = requests.get('http://apilayer.net/api/validate', params={'access_key': '5d0e36b0ce7208b266d3b7ab51d01e90', 'number': '+79655824681'})
print(response.json())

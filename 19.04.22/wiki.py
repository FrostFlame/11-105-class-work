import urllib
from urllib import parse
from urllib.request import urlopen

url = 'https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D0%BD%D0%B0%D0%BD'
uri = 'https://ru.wikipedia.org/wiki/Банан'
root = 'https://ru.wikipedia.org/'

string = 'Банан'
new_string = urllib.parse.quote(string)
# print(new_string)

# print(urllib.parse.unquote(new_string))

with urlopen(url) as web_page:
    with open('my_html.html', 'w', encoding='utf-8') as file:
        file.write(web_page.read().decode('utf-8'))

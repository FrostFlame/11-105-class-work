import re
import urllib
from urllib import parse
from urllib.request import urlopen

url = 'https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D0%BD%D0%B0%D0%BD'
uri = 'https://ru.wikipedia.org/wiki/Банан'
root = 'https://ru.wikipedia.org/'

string = 'Банан'
# new_string = urllib.parse.quote(string)
# print(new_string)

# print(urllib.parse.unquote(new_string))

with urlopen(url) as web_page:
    # with open('my_html.html', 'w', encoding='utf-8') as file:
    #     file.write(web_page.read().decode('utf-8'))
    content = web_page.read().decode('utf-8')
    links = {a for a in map(lambda x: urllib.parse.unquote(x), re.findall('/wiki/([A-Za-z0-9%_]*?)"', content)) if a}

# print(links)
all_links_set = set()
START = 'Банан'
FINISH = 'Пиратство'
MAX_ITER = 3

def find_path(links_list, result='', iter=0):
    for link in links_list:
        if link in all_links_set:
            continue
        all_links_set.add(link)
        print(f'{result} -> {link}')
        if link == FINISH:
            return f'{result} -> {link}'
        url = root + urllib.parse.quote(link)
        links = get_links(url)
        if iter < MAX_ITER - 2:
            result = find_path(links, result=f'{result} -> {link}', iter=iter+1)
    return ''


def get_links(link):
    with urlopen(url) as site:
        content = site.read().decode('utf-8')
        return {a for a in map(lambda x: urllib.parse.unquote(x), re.findall('/wiki/([A-Za-z0-9_%]*?)"', content)) if a}


print(find_path(links, result=START))
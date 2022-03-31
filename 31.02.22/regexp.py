import re

print(re.match('D', 'Damir'))
print(re.match('D', '5Damir'))
print(re.fullmatch('Damir', 'Damir'))
print(re.search('D', '5DamirD'))

pattern = re.compile('D')
pattern.match('Damir')
pattern.fullmatch('Damir')
pattern.search('Damir')


# . * + ? [] () \ |


# print(r'456\t456\n456\t456\n')


print(re.findall(r'.', 'asdsadadasasfsfddv54656499849_____()()(....'))
print(re.findall(r'[0123456789][0123456789][0123456789]', 'asdsadadasasfsfddv54656499849_____()()(....'))
print(re.findall(r'[0123456789]{3}', 'asdsadadasasfsfddv54656499849_____()()(....'))
print(re.findall(r'[0-9]{3}', 'asdsadadasasfsfddv54656499849_____()()(....'))
print(re.findall(r'\d{3}', 'asdsadadasasfsfddv54656499849_____()()(....'))
print(re.findall(r'\D{3}', 'asdsadadasasfsfddv54656499849_____()()(....'))
print(re.findall(r'\w{3}', 'asdsadadasasfsfddv54656499849_____()()(....'))
print(re.findall(r'\W{3}', 'asdsadadasasfsfddv54656499849_____()()(....'))
print(re.findall(r'[0-5a_]', 'asdsadadasasfsfddv54656499849_____()()(....'))

"""* + ?"""

print(re.findall(r'ab*', 'abbbbbbcabbbbabba'))
print(re.findall(r'ab+', 'abbbbbbcabbbbabba'))
print(re.findall(r'ab?', 'abbbbbbcabbbbabba'))

string = '<a href="/wiki/banana">Банан</a> assadsa' \
         'sadadadas <a href="/wiki/apple">Яблоко</a>'

print(re.findall(r'href="/wiki/.*"', string))
print(re.findall(r'href="/wiki/.*?"', string))

print(re.findall(r'ab*?', 'abbbbbbcabbbbabba'))
print(re.findall(r'ab+?', 'abbbbbbcabbbbabba'))
print(re.findall(r'ab??', 'abbbbbbcabbbbabba'))


import regex

string = 'asdasdafsafafacadasca'

print(re.findall(r'\w{3}', string))
print(regex.findall(r'\w{3}', string, overlapped=True))


string = 'asdsda a64d5as a65d4as admin@adm.in user@mail.ru 8-800-555-35-35 8-965-585-46-46'

print(re.findall(r'\w{2,10}@\w{2,10}\.\w{2,5}', string))
print(re.findall(r'\d-\d{3}-\d{3}-\d{2}-\d{2}', string))

print(re.findall(r'w\w{3}|s\w{3}', 'sentences consist of words worms'))


string = 'The quick brown fox jumps over the lazy dog'

pattern = r'\b[eyuioaEYUIOA]\w*'
print(re.findall(pattern, string))
pattern = r'\b[^ eyuioaEYUIOA]\w*'
print(re.findall(pattern, string))

string = 'sdg^46d;g4dgf^d4;6v4f84;^d4h5c4^c;1b498;f ;f^d4 dvd ^4d;g4d6gd--4-'
print(re.split(r'[\^;.+?*]', string))

string = 'Он -------- серо-бур-малиновая редиска ' \
         '>>>>>>:)' \
         'А не кот ' \
         'www.kot.ru'
# pattern = r'\b[\w-]+\b[ .]'
pattern = r'\w[\w-]*|\w'
print(re.findall(pattern, string))


"""Группы"""

string = 'admin@adm.in user@mail.ru'

print(re.findall(r'(\w{2,10})@(\w{2,10})\.\w{2,5}', string))

string = 'admin@admin.ru user@mail.ru re@re.ru abra@cadabra.com'

print(re.findall(r'(?P<name>\w{2,10})@(?P=name)\.\w{2,5}', string))

"""lookahead"""
# print(re.findall(r'\w+(?=\.ru)', string))
# print(re.findall(r'\w+(?!\.ru)', string))

pattern = re.compile(r'Isaac (?=Asimov)')
print(re.findall(pattern, 'Isaac Asimov'))
print(re.findall(pattern, 'Isaac '))

"""lookbehind"""
pattern = re.compile(r'(?<!Isaac) Asimov')
print(re.findall(pattern, 'Isaac Asimov'))
print(re.findall(pattern, ' Asimov'))


string = '2*(9+6)-45+3'
pattern = re.compile(r'(?<=\+)\d+')
print(re.findall(pattern, string))


print(r'456\t456\n456\t456\n')


st = 'aaabaaaabaabaaaa'
print(re.findall(r'(?<!a)(?:aa)+b', st))

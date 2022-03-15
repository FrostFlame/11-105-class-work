from types import SimpleNamespace

"""
    Анонимные классы
"""

sn = SimpleNamespace(name='Ibaa', surname='Hasan', hair_color='black')
sn2 = SimpleNamespace(name='Ibaa', surname='Hasan', hair_color='black')

print(sn)

print(sn == sn2)


sn3 = SimpleNamespace(**{'red': 3, 'height': 7.56, 'name': 'seven'})
print(sn3)

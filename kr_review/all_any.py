def foo(x):
    print(str(x) + ' is ' + str(bool(x)))


# foo(0)
# foo([])
# foo(False)
# foo('')


x = [1, True, ['asdsad'], 'casc']
# any all
if any(x):
    print('any')

if all(x):
    print('all')

a = None
b = False
c = []
d = ''
e = 0

y = a or b or c or d or e or 'Default value'
print(y)

'''LBLY      EAFP'''

x = {1: 1, 2: 2}

for key in range(1, 4):
    if key in x:
        print(x[key])

    try:
        print(x[key])
    except KeyError:
        print('ой, ошибка')

    print(x.get(key, 999))


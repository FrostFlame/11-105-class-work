def foo(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


if __name__ == '__main__':
    x = foo(5)
    print(x)
    x = foo(1)
    print(x)

from collections import namedtuple

MyTuple = namedtuple('MyTuple', ['x', 'y'])

p = MyTuple(x=5, y=4)
print(p)

print(p[0], p[1])

print(p.x, p.y)

a = [3, 4]
a = MyTuple._make(a)
print(a)

print(a._asdict())


from collections import deque

d = deque('qwerty')
for elem in d:
    print(elem.upper())

d.append('5')
d.appendleft('6')
print(d)

print(d.pop())
print(d.popleft())

print(d)
d.rotate(-1)
print(d)


from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrant'}
adjustment = {'art': 'van gogh', 'opera': 'carmen'}
my_map = ChainMap(adjustment, baseline)
print(my_map)
baseline['red'] = 'asdasda'
print(my_map)

from collections import Counter

c = Counter('asdasdsaadaduihlhggfbfd')
d = Counter({'red': 4, 'blue': 7})
e = Counter(coffee=6, eggs=5, tomatoes=7)

print(c['s'])
print(d['red'])
print(e['tomatoes'])

print(sorted(c.elements()))

print(c.most_common())

f = Counter(eggs=4, tomatoes=1, tea=3)
print(e+f)

from collections import OrderedDict
d = OrderedDict.fromkeys('abcde')
print(''.join(d.keys()))
print(d)

print(d.popitem(last=False))
print(d)

d.move_to_end('c', last=True)
print(d)

from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4),
     ('red', 1), ('blue', 4)]
d = dict()

for key, value in s:
    if key not in d:
        d[key] = [value]
    else:
        d[key].append(value)
print(d)

def_dict = defaultdict(list)
for key, value in s:
    def_dict[key].append(value)
print(def_dict)

set_dict = defaultdict(set)
for key, value in s:
    set_dict[key].add(value)
print(set_dict)
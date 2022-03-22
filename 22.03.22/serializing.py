import json
import pickle
from json import JSONEncoder
from typing import Any

a = dict(
    int_list=[1, 2, 3],
    text='string',
    boolean=True,
    number=322,
    none=None
)

class B:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return 'Я объект B, вот мой а: %s' % a


b = B(a)
# print(b)

x = pickle.dumps(b)
pickle.dump(b, open('../17.03.22/simple-pickle.pkl', 'wb'))

y = pickle.loads(x)
# print(y)

z = pickle.load(open('../17.03.22/simple-pickle.pkl', 'rb'))
# print(z)


class MyJsonEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__


# x = MyJsonEncoder().encode(b)
# print(x)

x = json.dumps(b, cls=MyJsonEncoder)
print(x)

y = json.loads(x)
print(y)


# x = json.dumps(jsonpickle.encode(b))
# print(x)
# y = json.loads(x)
# print(y)
# z = jsonpickle.decode(y)
# print(z)

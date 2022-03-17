import pickle

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
print(b)

x = pickle.dumps(b)
pickle.dump(b, open('simple-pickle.pkl', 'wb'))

y = pickle.loads(x)
print(y)

z = pickle.load(open('simple-pickle.pkl', 'rb'))
print(z)



print(type('5'))
print(type(5))


def bar(self, x):
    return x * 3


class A:
    def baz(self):
        print('10')


class B:
    pass


MyClass = type('X', (A, B), {'a': 'Foo', 'b': 13, 'foo': lambda self, x: x * 2, 'bar': bar})
o2 = MyClass()

print(o2.a)
print(o2.foo(10))
print(o2.bar(10))
o2.baz()

print(type(o2))
print(o2.__class__)


print(callable(1))
print(callable('as'))
print(callable(MyClass))
print(callable(o2))
print(callable(bar))


class Test:
    a = 5
    b = 6

    def __init__(self):
        self.color = 'blue'

    def __call__(self, *args, **kwargs):
        print('Called')

    def foo(self):
        pass

    def _bar(self):
        pass


t = Test()
t()
print(callable(t))


print(dir([1, 2, 3]))
print(dir(['asdasd', 'asdsa', 'cxv']))
print(dir(Test))
print(dir(t))


print(hasattr(t, 'a'))
print(getattr(t, 'a'))
delattr(Test, 'a')
print(hasattr(Test, 'a'))
print('Объект', hasattr(t, 'a'))
# print(Test.a)

t2 = Test()
print(hasattr(t2, 'a'))

print(help(5))
setattr(Test, 'bar', 456)


print(t.__class__)
print(Test.__class__)
print(int.__class__)
print(str.__class__)


class A:
    pass

class B:
    pass

class C(A, B):
    pass

c = C()
print(C.__bases__)


print(dir(Test))
print(Test.__dict__)
print(dir(t))
print(t.__dict__)


class A:
    __slots__ = ['obj_attr']
    name = 'name'
    color = 'color'

    def __init__(self):
        self.obj_attr = 5


a = A()
a.obj_attr = 7
# a.b = 6
setattr(A, 'z', 7)
print(a.z)


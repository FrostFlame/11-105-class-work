class A:
    name = 'A'

    def __init__(self, color):
        self.color = color

    def foo(self):
        print(self.name, self.color)

    @classmethod
    def bar(cls):
        print(cls.name)

    @staticmethod
    def baz():
        print('Я статический')

a = A('blue')
b = A('red')
a.foo()
A.foo(a)
A.foo(b)

A.bar()
a.bar()

a.baz()
A.baz()



class Human:
    def __init__(self, age):
        self.age = age

    @classmethod
    def is_adult(cls, age):
        return age > 18

h = Human(19)
# z = Human(20)
print(h.is_adult(h.age))

print(Human.is_adult(20))
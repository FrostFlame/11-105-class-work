class MyClass:
    num = 5
    _num = 6
    __num = 7
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return 5

    def __str__(self):
        return self.name

obj = MyClass(4)
print(obj.num)
print(obj._num)
print(obj._MyClass__num)

asdsa = MyClass('Ivan')
print(str(asdsa))

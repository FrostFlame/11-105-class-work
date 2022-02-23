from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def foo(self):
        print('bla-bla')

# my_object = MyAbstractClass()
# my_object.foo()

class MyRealClass(MyAbstractClass):

    def foo(self):
        super().foo()
        print('i am real class')


my_real_object = MyRealClass()
my_real_object.foo()
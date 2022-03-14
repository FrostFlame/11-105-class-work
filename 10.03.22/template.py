from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.hook1()
        self.base_operation2()
        self.required_operation2()
        self.hook2()
        self.base_operation3()

    def base_operation1(self):
        print('Абстрактный класс: базовая операция 1')

    def base_operation2(self):
        print('Абстрактный класс: базовая операция 2')

    def base_operation3(self):
        print('Абстрактный класс: базовая операция 3')

    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass


class ConcreteClass1(AbstractClass):
    def required_operation1(self):
        print('Конкретный класс 1: обязательная операция 1')

    def required_operation2(self):
        print('Конкретный класс 1: обязательная операция 2')

class ConcreteClass2(AbstractClass):
    def required_operation1(self):
        print('Конкретный класс 2: обязательная операция 1')

    def required_operation2(self):
        print('Конкретный класс 2: обязательная операция 2')

    def hook1(self):
        print('Конкретный класс 2: необязательная операция')

a = ConcreteClass1()
b = ConcreteClass2()

a.template_method()
print('--------------------------')
b.template_method()
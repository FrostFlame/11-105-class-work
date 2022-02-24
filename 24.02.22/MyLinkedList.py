from abc import abstractmethod, ABC


class MyAbstractList(ABC):
    @abstractmethod
    def append(self, value):
        pass

    @abstractmethod
    def insert(self, pos, value):
        pass

    @abstractmethod
    def pop(self, pos):
        pass

    @abstractmethod
    def size(self):
        pass


class MyNode:
    def __init__(self, value, next_node):
        self.__value = value
        self.__next = next_node

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node

    def __str__(self):
        return str(self.__value)


class MyLinkedList(MyAbstractList):
    def __init__(self, iterable):
        next_node = None
        for elem in reversed(iterable):
            self.head = MyNode(elem, next_node)
            next_node = self.head

    def append(self, value):
        elem = self.head
        while elem.get_next() is not None:
            elem = elem.get_next()
        elem.set_next(MyNode(value, None))

    def insert(self, pos, value):
        if pos > self.size():
            raise IndexError
        elem = self.head
        for i in range(pos - 1):
            elem = elem.get_next()
        new_elem = MyNode(value, elem.get_next())
        elem.set_next(new_elem)

    def pop(self, pos):
        if pos >= self.size():
            raise IndexError
        elem = self.head
        for i in range(pos - 1):
            elem = elem.get_next()
        result = elem.get_next().get_value()
        elem.set_next(elem.get_next().get_next())
        return result

    def size(self):
        result = 0
        elem = self.head
        while elem is not None:
            elem = elem.get_next()
            result += 1
        return result

    def __str__(self):
        result = ''
        elem = self.head
        while elem is not None:
            result += str(elem) + ' -> '
            elem = elem.get_next()
        result += 'None'
        return result


if __name__ == '__main__':
    my_list = MyLinkedList([3, 2, 1])
    print(my_list)

    my_list.append(7)
    print(my_list)

    try:
        my_list.insert(10, 5)
        print(my_list)
    except IndexError as e:
        print('Неверный индекс')

    try:
        x = my_list.pop(1)
        print(x)
        print(my_list)
    except IndexError as e:
        print('Неверный индекс')

    print(my_list.size())

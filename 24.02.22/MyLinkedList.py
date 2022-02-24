from abc import abstractmethod, ABC


class MyAbstractList(ABC):
    @abstractmethod
    def append(self, value):
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

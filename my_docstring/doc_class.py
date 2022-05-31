import doctest


class Foo:
    """
    >>> a = Foo(5)
    >>> a.mul_2()
    10
    """
    def __init__(self, n):
        self.n = n

    def mul_2(self):
        return self.n * 2

    def mul_3(self):
        return self.n * 3


if __name__ == '__main__':
    # doctest.testmod()
    doctest.testfile('test.txt')

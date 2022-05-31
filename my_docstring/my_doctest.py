import doctest


def foo(x, y):
    """
    Return result depending on parity

    :param x: int
    :param y: int
    :return: int

    If both are odd return sum
    >>> foo(1, 3)
    4

    If both are even return sub
    >>> foo(2, 4)
    -2
    >>> foo(1, 2)
    2
    >>> foo(2, 3)
    0
    >>> foo(1.0, 2)
    Traceback (most recent call last):
    ...
    ValueError: x and y should be int
    """
    if type(x) is float or type(y) is float:
        raise ValueError('z and y should be int')
    return 4


def bar(n):
    """
    >>> bar(-2)
    0
    >>> bar(10)
    11
    """
    return n if n > 0 else 0


if __name__ == '__main__':
    doctest.testmod()

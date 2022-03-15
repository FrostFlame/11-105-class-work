def foo(a):
    """Local"""
    x = 2
    return x + a


# print(foo(5))
# print(x)


def foo(a):
    """Local"""
    x = 2

    def bar():
        """Enclosure"""
        print('x=%i' % x)
        return a + x
    return bar()


# foo(5)


"""Global"""
X = 5
ERROR_MESSAGE = 'asdas'
CONFIG_PATH = 'dasdsad'


"""built-in"""

# len()
# str()
# sum()


def mul(a, b):
    return a * b


# print(mul(5, 4))
# print(mul(5, 7))


def mul5(a):
    return mul(5, a)


# print(mul5(7))
# print(mul5(4))


def mul(a):
    def helper(b):
        return a * b
    return helper


# print(mul(5)(2))

mul6 = mul(6)

# print(mul6(7))


def func1(a):
    x = a * 3

    def func2(b):
        nonlocal x
        x = x * 2
        return b + x
    return func2


test_func = func1(4)

# print(test_func(7))
# print(test_func(7))
# print(test_func(7))
# print(test_func(7))


tpl = lambda a, b: (a, b)

a = tpl(1, 2)
print(a)

b = tpl(3, a)
print(b)

c = tpl(a, b)
print(c)

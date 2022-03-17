a, b = 4, 6


x, y, z = range(3)

# print(x, y, z)

a = [1, 2, 3]

x, y, z = {'1', '2', '3'}

# print(x, y, z)


*a, = 1, 2, 3, 'asdsa'
# print(a)

a, b, *c = 1, 2, 10, 5, 'asd'
# print(a)
# print(b)
# print(c)


a = range(10)
# print(*a)
a = [1, 2, 0, 0, 0, 0, 0]
a, b, *_ = a

# print(a)
# print(b)
# print(_)

def return_3_values():
    return 1, 2, 3


a, *b = return_3_values()
# print(a)
# print(b)
# print(c)


a = [1, 2, 3]
b = (4, 5, 6)
c = [7, 8, 9]

# e = a + b + c
e = [*a, *b, *c, *range(10)]
# print(e)


numbers = {'one': 1, 'two': 2, 'three': 3, 'a': 156}
letters = {'a': 'A', 'b': 'B', 'c': 'C'}

combination = {**numbers, **letters}
# print(combination)


def foo(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


foo(a=7, b=7, name='Name', color='blue')




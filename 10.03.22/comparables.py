from functools import total_ordering, cmp_to_key


# @total_ordering
class A:
    def __str__(self):
        return ' '.join([self.name, self.color])

    def __repr__(self):
        return ' '.join([self.name, self.color])

    def __init__(self, name, color):
        self.name = name
        self.color = color

    # ==
    # def __eq__(self, other):
    #     return (self.name, self.color) == (other.name, other.color)

    # !=
    # def __ne__(self, other):
    #     pass

    # <
    # def __lt__(self, other):
    #     pass

    # >
    # def __gt__(self, other):
    #     return len(self.name) > len(other.name)

    # # <=
    # def __le__(self, other):
    #     pass
    #
    # # >=
    # def __ge__(self, other):
    #     pass


# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)


a = A('firsta', 'red')
b = A('firstb', 'red')
c = A('secondc', 'blue')


d = [a, b, c]


def compare(x, y):
    if baz(x, y):
        return -1
    elif baz(y, x):
        return 1
    else:
        return 0


def baz(x, y):
    return len(x.name) % 2 == 1


d = sorted(d, key=cmp_to_key(compare))
print(d)

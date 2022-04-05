from functools import reduce
# 1^1 == 1
# 9^1
# 153 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

func = lambda a: sum([int(c)**len(str(a)) for c in str(a)]) == a

print(func(5))



def foo(x):
    sum = []
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            sum.append(i)
    return sum

print(foo(10))

foo1 = lambda x: reduce(lambda x, y: x + y, filter(lambda x: x % 3==0 or x % 5 ==0, range(x)))
# foo2 = lambda

print(foo1(10))
# 3 + 5 + 6 + 9 = 23



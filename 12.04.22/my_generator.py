from time import sleep


def my_generator(st):
    st = st + st[::-1]
    while True:
        for i in st:
            x = yield i
            print(x)
        for i in st[::-1]:
            x = yield i
            print(x)


# for i in my_generator(5):
#     print(i)
#     sleep(1)


class MyGenerator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            s = 0
            k = 0
            tmp = i
            while tmp != 0:
                k += 1
                tmp = tmp // 10
            tmp = i
            while tmp != 0:
                s += (tmp % 10) ** k
                tmp = tmp // 10
            if s == i:
                yield i


# a = MyGenerator(1000)
# for i in a:
#     print(i)
# print(next(a))
# print(a.send(10))

b = my_generator('asd')
print(next(b))
print(b.send('asdas'))


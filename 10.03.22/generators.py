# def my_generator(val):
#     i = 0
#     while i < val:
#         print('---------------')
#         yield i
#         print('asdasdadadad')
#         yield i
#
#         yield i + 1
#         i += 1
#
# my_gen = my_generator(5)
#
# # for i in my_generator(10):
# #     print(i)
#
# print(list(my_gen))
from time import time, sleep


def gen_filename():
    while True:
        pattern = 'file-{}.txt'
        t = int(time() * 1000)

        yield pattern.format(t)

        sleep(1)
        sum = 234 + 234
        print(sum)

gen = gen_filename()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


def gen1(x):
    for i in x:
        yield i


def gen2(n):
    for i in range(n):
        yield i

g1 = gen1('azat')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass

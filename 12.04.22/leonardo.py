from functools import reduce

leo = lambda x: 1 if x == 1 or x == 2 else leo(x - 1) + leo(x - 2) + 1
leo1 = lambda x: [leo(i) for i in range(1, x + 1)]
leo2 = lambda x: reduce(lambda x, y: x + y, filter(lambda x: x % 3 == 0, leo1(x)))
print(leo1(10))
print(leo2(10))

my_len = lambda x: my_len(x // 10) + 1 if x >= 10 else 1
leo3 = lambda x: reduce(lambda x, y: x + y**(len(str(y))), leo1(x), 0)
# leo3 = lambda x: reduce(lambda x, y: x + y**(my_len(str(y))), leo1(x), 0)
print(leo3(3))
print(my_len(1))
print(my_len(10))
print(my_len(100))
print(my_len(46456))

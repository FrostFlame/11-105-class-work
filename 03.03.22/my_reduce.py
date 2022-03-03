from functools import reduce

num = [1, 5, 10, 42, 64]
# res = 1
# for e in num:
#     res *= e
# print(res)

res = reduce(lambda x, y: x * y, num)
print(res)

# reduce(function, iterable)
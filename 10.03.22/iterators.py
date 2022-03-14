a = ['asdas', 'sdss', 56156, True]

a_iter = iter(a)

# print(a_iter)
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))

# for i in a_iter:
#     print('-----------------')
#     print(i)


class MyIterator:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


my_iter = iter(MyIterator())

# print(next(my_iter))
for i in range(5):
    print(next(my_iter))


print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


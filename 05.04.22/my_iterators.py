class MyIterator:
    def __init__(self, array, steps):
        self.array = array
        self.steps = steps
        self.length = len(array)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.steps:
            answer = self.array[self.index % self.length]
            self.index += 1
            return answer
        else:
            raise StopIteration


a = MyIterator([1, 2, 3], 2)


# for i in a:
#    print(i)
# print(next(a))

def generator(array):
    a = len(array)
    k = 0
    while True:
        yield array[k]
        k += 1
        if k == a:
            k = 0


# for i in generator([1,2,3,4,5,6]):
#     print(i)


def gen(x):
    yield 1
    yield 1
    m = 1
    n = 1
    for i in range(x - 2):
        yield m + n
        n, m = m+n,n
for i in gen(5):
    print(i)

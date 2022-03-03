# a = 5
# b = 6
# a, b = b, a
# print(a, b)


#Lambda

def square(x):
    return x ** 2

# square = lambda x: x ** 2
#  labmda argument: expression

print(square(5))

maxi = lambda x, y: x + 5 if x > y else y / 10

print(maxi(5, 10))


def transform(n):
    return lambda x: x * n


f = transform(3)
print(f(4))

f = transform(10)
print(f(4))
print(f(5))



# Map

# squares = [i ** 2 for i in range(1, 10, 2)]
# print(squares)

squares = list(map(square, range(1, 10, 2)))
# map(function, iterable)
print(squares)

squares = list(map(lambda x: x ** 2, range(1, 10, 2)))
print(squares)


num1 = [1, 2, 3, 7]
num2 = [4, 5, 6, 7]

result = list(map(lambda x, y: x + y, num1, num2))
print(result)


a = 10
b = [1, 2, 3]

print(type(a) == int)
print(isinstance(a, (list, tuple, float)))

class A(list):
    pass

a = A()

print(type(a) == list)
print(isinstance(a, list))

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)  # == print(id(a) == id(b))

a = b
print(a is b)

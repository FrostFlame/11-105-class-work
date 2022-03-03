# Filter

a = [1, 5, 10, 15, 64, 105, 120]

b = list(filter(lambda x: x % 2 != 0, a))
# filter(function, iterable)
print(b)

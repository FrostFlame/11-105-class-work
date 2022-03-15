from functools import partial


def greet(greeting, separator, emphasis, name):
    print(greeting, separator, name, emphasis)

"""
partial
1 (n) -> 1 (n-k)

curring
1 (n) -> n (1)
"""
new_func = partial(greet, greeting='Hello', separator=',', emphasis='.')
new_func(name='Ivan')
new_func(name='Ibaa')


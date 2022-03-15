"""Карринг - curring"""


def greet(greeting, name):
    print('%s, %s' % (greeting, name))


# greet('Hello', 'Ivan')
# greet('Hello', 'Ibaa')
# greet('Hello', 'Olya')


def curried_greet(greeting):
    def greet(name):
        print('%s, %s' % (greeting, name))
    return greet


# greet_hello = curried_greet('Hello')
# greet_hello('Ivan')
# greet_hello('Ibaa')
#
# curried_greet('Ciao')('Katya')


def greet_deeply_curried(greeting):
    def w_separator(separator):
        def w_emphasis(emphasis):
            def greet(name):
                print(greeting, separator, name, emphasis)
            return greet
        return w_emphasis
    return w_separator


greet = greet_deeply_curried('Hello')('...')('.')
# greet('Ivan')
# greet('Katya')
# greet('Ibaa')


greet_deeply_curried = lambda greeting: lambda separator: lambda emphasis:\
    lambda name: print(greeting, separator, name, emphasis)


def my_decorator(func):
    def wrapper(arg1, arg2):
        print(arg1)
        func(arg1, arg2)
        print(arg2)
    return wrapper

@my_decorator
def foo(arg1, arg2):
    print('middle')

def decorator_maker(dec_arg1, dec_arg2):
    def decorator(func):
        def wrapper(arg1, arg2):
            result = func(arg1, arg2) + ' маршрут ' + dec_arg1 + ' - ' + dec_arg2 + ' ' + arg1 + ' - ' + arg2
            print(result)
        return wrapper
    return decorator

@decorator_maker('Казань', 'Владивосток')
def bar(arg1, arg2):
    return 'Поезд 1'



# foo(5, 4)

bar('15:30', '17:00')
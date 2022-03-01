print('Это файл 1')

class A():
    pass

def foo():
    print('Функция 1')



if __name__ == '__main__':
    a = A()
    print('Вызвано напрямую файл 1')
    foo()

from tests.calc import *


def test_add():
    a = 5
    b = 6
    if add(a, b) == a + b:
        print('Работает корректно')
    else:
        print('Ошибка')


def test_sub():
    a = 5
    b = 6
    if sub(a, b) == a - b:
        print('Работает корректно')
    else:
        print('Ошибка')

def test_div():
    a = 5
    b = 6
    if div(a, b) == a / b:
        print('Работает корректно')
    else:
        print('Ошибка')

def test_mul():
    a = 5
    b = 6
    if mul(a, b) == a * b:
        print('Работает корректно')
    else:
        print('Ошибка')
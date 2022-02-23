try:
    x = 5/0
except EOFError:
    pass
except ZeroDivisionError as e:
    pass
else:
    print('Ошибка не упала')
finally:
    print('Выполняюсь в любом случае')


print('Hello')

class MyException(BaseException):
    message = 'Моя ошибка, всё плохо'

try:
    raise MyException
except MyException as e:
    print(e.message)

print(5 + 5)
print('str' + 'def')
print(5 + 'def')
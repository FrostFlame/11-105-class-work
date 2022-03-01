ERROR_MESSAGE = 'Строка некорректна'
SUCCESS_MESSAGE = 'Строка корректна'


def is_correct(sequence):
    stack = []
    for a in sequence:
        if a in ['[', '(', '{']:
            stack.append(a)
        elif a == ']':
            if stack.pop() != '[':
                return ERROR_MESSAGE
        elif a == ')':
            if stack.pop() != '(':
                return ERROR_MESSAGE
        elif a == '}':
            if stack.pop() != '{':
                return ERROR_MESSAGE
        else:
            return ERROR_MESSAGE
    if stack:
        return ERROR_MESSAGE
    return SUCCESS_MESSAGE


if __name__ == '__main__':
    while True:
        print(is_correct(input('Введите строку: ')))

import locale
from contextlib import contextmanager

file = open('file.txt', 'r', encoding='utf-8')

# print(locale.getpreferredencoding())
text = file.read()
# print(text)

file = open('file1.txt', 'r', encoding='utf-8')
# file.write('123456789')
for line in file:
    print(line.strip())


# x = open('file1.txt', 'r', encoding='utf-8')
# print(x.read())
# # file.write('second line')
# print(x.read())

file.close()

file = open('file.txt', 'r', encoding='utf-8')
try:
    file.read()
finally:
    file.close()


with open('file.txt', 'w+', encoding='utf-8') as file:
    file.read()
    file.write('fv')

print('asd')


class File:
    def __init__(self, filename, method):
        self.file = open(filename, method, encoding='utf-8')

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with File('file.txt', 'r') as file:
    file.read()


@contextmanager
def open_file(name):
    f = open(name, 'r')
    yield f
    f.close()


with open_file('file.txt') as file:
    file.read()


x = b'\xf0\x9f\xa4\xa8'
y = x.decode('utf-8')
with open('file.bin', 'wb') as file:
    file.write(y.encode('utf-8'))

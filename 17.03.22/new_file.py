# coding: utf-8

a = u'string'
b = b'string'

print(type(a))
print(a)
print(type(b))
print(b)

c = a.encode('utf-8')
print(c)

x = bytes(10)
print(x)

y = bytes(range(20))
print(y)

x = bytes([50, 77, 64, 121, 127])
print(x)

print(chr(50))
print(ord(b'2'))

# z = bytes('Hello', encoding='utf-8')
# print(z)


print(b + x)
print(b * 5)
print(b[0])

x = bytes.fromhex('2E f0 F1 f2 ')
print(x)


print(type('string'[0]))
print(type('string'[0:1]))
print(type(b'string'[0]))
print(type(b'string'[0:1]))

print(list(b'string'))

b = bytearray(b'Hello world')

b[0] = ord(b'1')
print(b)


"""
    python2
    unicode str
    
    python3
    str     bytes
"""

x = '大三'
y = bytes(x, encoding='utf-8')
print(len(x))
print(y)
print(len(y))


# print('Привет'.encode('utf-8'))
# print(list('Привет'.encode('utf-8')))

x = b'\xf0\x9f\xa4\xa8'
y = x.decode('utf-8')
print(x)
print(y)

print(len(y))


data = b'\xbc cup of flour'
# print(data.decode('utf-8'))
print(data.decode('latin-1'))

# chardet

import io

b = io.BytesIO(b'abcdef')

value = b.getvalue()
print(value)
# print(type(value))

view = b.getbuffer()
view[2:4] = b'56'
# print(b.getvalue())


with open('byte.bin', 'wb', buffering=50) as file:
    while True:
        file.write(b'456\x04789\x26\n')

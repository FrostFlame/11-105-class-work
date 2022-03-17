import io

fp = io.StringIO()

fp.write('asdsaf\n')
print('Second line', file=fp)

print(fp.getvalue())


f = open('file.txt', 'r', encoding='utf-8')
f = io.StringIO('some initial value')


f = open('file.bin', 'rb')
f = io.BytesIO(b'initial binary value: \x00\x01')


f = open('file.bin', 'rb', buffering=0)
print(f.read())



import re
import socket


'''
socket.bind(address)
socket.listen()
socket.accept()
socket.recv()
socket.send()
socket.close()
'''

word = input()
guessed = '_' * len(word)
hangman = ''' +---+
 |   |
     |
     |
     |
     |
======='''


def update(st):
    if st[15] == ' ':
        return ''.join((st[:15], '0', st[16:]))
    elif st[22] == ' ':
        return ''.join((st[:22], '|', st[23:]))
    elif st[21] == ' ':
        return ''.join((st[:21], '/', st[22:]))
    elif st[23] == ' ':
        return ''.join((st[:23], '\\', st[24:]))
    elif st[23] == ' ':
        return ''.join((st[:23], '\\', st[24:]))
    elif st[28] == ' ':
        return ''.join((st[:28], '/', st[29:]))
    elif st[30] == ' ':
        return ''.join((st[:30], '\\', st[31:], '\nВы проиграли!'))


sock = socket.socket()
sock.bind(('', 50000))
sock.listen(10)
print('Server is running')

conn, addr = sock.accept()
print('connected: ', addr)
while not guessed.startswith(word) and not hangman.endswith('!'):
    data = conn.recv(1024).decode('utf-8')
    print(data)
    indexes = [_.start() for _ in re.finditer(data, word)]
    if indexes:
        for index in indexes:
            guessed = ''.join((guessed[:index], data, guessed[index + 1:]))
            if guessed == word:
                guessed += '\nВы победили!'
        conn.send(guessed.encode('utf-8'))
    else:
        hangman = update(hangman)
        conn.send(hangman.encode('utf-8'))
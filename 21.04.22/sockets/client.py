import socket

sock = socket.socket()
sock.connect(('localhost', 50000))

# while True:
data = b''
while not data.decode('utf-8').endswith('!'):
    sock.send(input().encode('utf-8'))

    data = sock.recv(1024)
    print(data.decode('utf-8'))

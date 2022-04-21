import socket

sock = socket.socket()
sock.connect(('localhost', 50000))

while True:
    sock.send(input().encode('utf-8'))

    data = sock.recv(1024)
    print(data.decode('utf-8'))

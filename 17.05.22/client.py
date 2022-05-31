import socket

sock = socket.socket()

sock.connect(('localhost', 50000))

while True:
    sock.send(bytes(input(), encoding='utf-8'))
    msg = sock.recv(1024)
    print(msg.decode('utf-8'))
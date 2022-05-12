import socket

sock = socket.socket()
sock.connect(('localhost', 50000))

while True:
    msg = sock.recv(1024).decode('utf-8')
    print(msg)

    msg = input().encode('utf-8')
    sock.send(msg)




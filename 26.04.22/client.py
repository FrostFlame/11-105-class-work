import socket

sock = socket.socket()
sock.connect(('10.150.136.6', 50000))

while True:
    sock.send(input().encode('utf-8'))

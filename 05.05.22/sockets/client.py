import socket
from time import sleep


while True:
    sock = socket.socket()
    sock.connect(('localhost', 50000))
    print(sock.recv(1024).decode())
    sock.close()
    sleep(5)


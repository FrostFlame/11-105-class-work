import socket
from itertools import cycle

sock = socket.socket()
sock.bind(('', 50000))

sock.listen(10)
conn1, _ = sock.accept()
conn2, _ = sock.accept()
conn_lst = [conn1, conn2]

conn1.send('You are first, start chat'.encode('utf-8'))

while True:
    conn = conn_lst.pop(0)
    msg = conn.recv(1024)

    conn_lst[0].send(msg)
    conn_lst.append(conn)

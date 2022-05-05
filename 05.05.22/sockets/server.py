import socket

sock = socket.socket()
sock.bind(('', 50000))

sock.listen(10)
for i in range(100):
    conn, _ = sock.accept()
    conn.send(str(i).encode('utf-8'))


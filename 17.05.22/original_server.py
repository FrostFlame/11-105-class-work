import socket

sock = socket.socket()
sock.bind(('', 50000))
sock.listen(10)

while True:
    conn, _ = sock.accept()

    while True:
        msg = conn.recv(1024)

        if not msg:
            break
        else:
            print(msg.decode('utf-8'))
            msg = 'Hello world'
            conn.send(msg.encode('utf-8'))
    conn.close()

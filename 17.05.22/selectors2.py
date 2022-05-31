import socket
import selectors

selector = selectors.DefaultSelector()

def server():
    server_sock = socket.socket()
    server_sock.bind(('', 50000))
    server_sock.listen(10)

    selector.register(fileobj=server_sock, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_sock):
    conn, _ = server_sock.accept()
    selector.register(fileobj=conn, events=selectors.EVENT_READ, data=send_message)


def send_message(conn):
    msg = conn.recv(1024)
    print(msg.decode('utf-8'))

    if msg:
        msg = 'Hello world'
        conn.send(msg.encode('utf-8'))
    else:
        selector.unregister(conn)
        conn.close()


def event_loop():
    while True:
        events = selector.select()

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()

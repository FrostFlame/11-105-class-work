import socket
from select import select

to_monitor = []

server_sock = socket.socket()
server_sock.bind(('', 50000))
server_sock.listen(10)


def accept_connection(server_sock):
    conn, _ = server_sock.accept()
    to_monitor.append(conn)


def send_message(conn):
    msg = conn.recv(1024)
    print(msg.decode('utf-8'))

    if msg:
        msg = 'Hello world'
        conn.send(msg.encode('utf-8'))
    else:
        to_monitor.remove(conn)
        conn.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])

        for sock in ready_to_read:
            if sock is server_sock:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_sock)
    event_loop()

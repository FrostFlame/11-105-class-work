import random
import socket
import time
from time import sleep
import asyncio


async def send(sock, msg=b'ping', once=False):
    while True:
        time.sleep(2)
        print('Отправлю сообщение ' + msg.decode('utf-8'))
        await asyncio.get_event_loop().sock_sendall(sock, msg)
        if once:
            break


async def recv(sock):
    while True:
        msg = await asyncio.get_event_loop().sock_recv(sock, 1024)
        print(msg.decode('utf-8'))
        await send(sock, msg, True)


async def main():
    sock = socket.socket()
    sock.bind(('', 50000))

    sock.listen(10)

    conn, _ = sock.accept()
    asyncio.get_event_loop()

    while True:
        await asyncio.gather(send(conn), recv(conn))


if __name__ == '__main__':
    asyncio.run(main())

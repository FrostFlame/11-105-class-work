import asyncio
import socket
import aioconsole


async def send(sock):
    while True:
        msg = await aioconsole.ainput()
        print('Отправлю сообщение ' + msg)
        await asyncio.get_event_loop().sock_sendall(sock, msg.encode('utf-8'))


async def recv(sock):
    while True:
        msg = await asyncio.get_event_loop().sock_recv(sock, 1024)
        print(msg.decode('utf-8'))


async def main():
    sock = socket.socket()
    sock.connect(('localhost', 50000))

    await asyncio.gather(recv(sock), send(sock))


if __name__ == '__main__':
    asyncio.run(main())

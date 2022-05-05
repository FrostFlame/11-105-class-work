import socket
from itertools import cycle

sock = socket.socket()
sock.bind(('10.150.136.6', 50000))
print('Server started')

sock.listen(2)

conn1, addr1 = sock.accept()
print(f'Connected {addr1}')
conn2, addr2 = sock.accept()
print(f'Connected {addr2}')
conn1.settimeout(5)
conn2.settimeout(5)

for conn in cycle([conn1, conn2]):
    try:
        msg = conn.recv(1024)
        conn.send()
        print(msg.decode('utf-8'))
    except Exception as e:
        print(f'{conn} {e}')

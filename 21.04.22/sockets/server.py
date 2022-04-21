import socket


'''
socket.bind(address)
socket.listen()
socket.accept()
socket.recv()
socket.send()
socket.close()
'''

sock = socket.socket()
sock.bind(('', 50000))
sock.listen(10)
print('Server running')
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    data = data.decode('utf-8')
    print(data)
    conn.send(data.upper().encode('utf-8'))



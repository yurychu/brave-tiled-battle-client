import socket

HOST = ''
PORT = 9090

sock = socket.socket()

sock.bind((HOST, PORT))
print('binding to {} {} ...'.format(HOST, PORT))

sock.listen(1)

print("starting listen...")
conn, addr = sock.accept()
print('Connect:', addr)

while True:
    data = conn.recv(1024)
    print(data)
    if not data:
        break
    conn.send(data.upper())

conn.close()

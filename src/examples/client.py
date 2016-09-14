import socket

HOST = 'localhost'
PORT = 9090

sock = socket.socket()
sock.connect((HOST, PORT))

message = b'hello meen'
sock.send(message)

data = sock.recv(1024)
sock.close()

print(data)

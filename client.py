import socket
import sys
from socket import gethostbyname

#step 1: create a client socket
client_socket = socket.socket()

#step 2: connect() to the server address and port
server_addr = ('127.0.0.1',5000) #replace 127.0.0.1 by the ip address of the server
client_socket.connect(server_addr)

#step 3: send
msg = "hello there brother Its working"
client_socket.sendall(msg.encode('utf-8'))
print(sys.stderr)

#step 4: close()
client_socket.close()

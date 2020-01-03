import socket
import sys
import os
from socket import gethostbyname

msg = ""

#step 1: create a socket
server_socket = socket.socket()

#step 2: bind the socket to server_address and a dedicated port
server_address = (gethostbyname('0.0.0.0'),5000)
server_socket.bind(server_address)

#step 3: put the machine into server mode
server_socket.listen(1)

#step 4: accept a connection
while True:
    connection, client_addr = server_socket.accept()
    
    #step 5: receive data
    while True:
        data = connection.recv(16)
        if data:
            msg += data.decode('utf-8')
        else:
            break
    
    if len(msg) > 0:
        print(msg)
        break

print("client address is: ",client_addr)

#step 5: close
server_socket.close()

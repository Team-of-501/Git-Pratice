"""
communicate with luoque
"""
import socket

socket_client = socket.socket()
socket_client.connect(('127.0.0.1', 8008))

while True:
    msg = input()
    if msg == 'exit':
        break
    socket_client.send(msg.encode("UTF-8"))
    recv_data = socket_client.recv(1024).decode("UTF-8")
    print(recv_data)
socket_client.close()

"""
custom async socket server
"""

import socket
from select import select

HOST = "localhost"
PORT = 8080

server_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_s.bind((HOST, PORT))
server_s.listen()
print(f"SERVER {HOST} : {PORT}")


def accept_connection(server: socket.socket):
    client, addr = server.accept()
    print(f"CONNECTION : {addr}")
    sockets.append(client)


def respond(client: socket.socket):
    request = client.recv(1024)

    if request:
        client.sendall(b"Well received")
    else:
        client.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(sockets, [], [])

        for s in ready_to_read:
            if s is server_s:
                accept_connection(s)
            else:
                respond(s)


if __name__ == '__main__':
    sockets = [server_s]
    event_loop()

"""
custom async socket server
"""

import socket
import selectors

HOST = "localhost"
PORT = 8080

selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=client_connection)


def client_connection(server: socket.socket):
    client_s, addr = server.accept()
    print(f"CONNECTED : {addr}")

    selector.register(fileobj=client_s, events=selectors.EVENT_READ, data=response)


def response(client: socket.socket):
    request = client.recv(1024)

    if request:
        client.sendall(b"Well received")
    else:
        selector.unregister(client)
        client.close()


def event_loop():
    while True:
        events = selector.select()  # (key, events)

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()


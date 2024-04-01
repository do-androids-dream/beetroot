"""
custom async server based on generators
"""

import socket
from select import select


HOST = "localhost"
PORT = 8080

tasks = []
to_read = {}
to_write = {}


def server():
    server_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_s.bind((HOST, PORT))
    server_s.listen()

    print(f"SERVER {HOST} : {PORT}")

    while True:
        yield ("read", server_s)

        client_s, addr = server_s.accept()

        print(f"CONNECTED {client_s}")
        tasks.append(response(client_s))


def response(client_s: socket.socket):
    while True:

        yield ("read", client_s)
        request = client_s.recv(1024)

        if not request:
            break

        else:
            yield ("write", client_s)
            client_s.sendall(b"Well received")

    client_s.close()


def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)

            purpose, sock = next(task)

            if purpose == "read":
                to_read[sock] = task

            if purpose == "write":
                to_write[sock] = task

        except StopIteration:
            pass


if __name__ == '__main__':
    tasks.append(server())
    event_loop()

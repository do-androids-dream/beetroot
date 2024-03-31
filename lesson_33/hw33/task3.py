"""
Echo server with multiprocessing

Create a socket echo server that handles each connection using the multiprocessing library.
"""

import socket
import multiprocessing

HOST = "localhost"
PORT = 8080

server_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_s.bind((HOST, PORT))

server_s.listen(5)
print(f"Server is listening on {HOST}:{PORT}")


def handle_connection(con: socket.socket):
    while True:
        try:
            data = con.recv(1024)
            echo_resp(data, con)
        except Exception:
            continue


def echo_resp(data, con: socket.socket):
    con.sendall(data)


while True:
    try:
        connection, address = server_s.accept()
        t = multiprocessing.Process(target=handle_connection, args=(connection, ))
        t.run()
    except Exception:
        connection.close()

"""
Echo server with threading

Create a socket echo server which handles each connection in a separate Thread
"""

import socket
import threading

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
        t = threading.Thread(target=handle_connection, args=(connection, ), daemon=True)
        t.run()
    except Exception:
        connection.close()

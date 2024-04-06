#  handle client -> threads
#  response -> threads
######
#  handle_client - client socket and ip-port
import threading
from threading import Thread
import socket
from queue import Queue
from typing import List

HOST = "127.0.0.1"
PORT = 8080
connections: List[socket.socket] = []
msgs_queue = Queue()


def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    while True:
        try:
            data = client_socket.recv(1024)
        except Exception as e:
            print(type(e), e)
            break

        if not data:
            break

        msgs_queue.put(data)


def main():
    backlog = 5
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(backlog)
    print(f"Server listening on {HOST}:{PORT}")

    message_thread = threading.Thread(target=response_all, args=(connections, msgs_queue), daemon=True)
    message_thread.start()
    try:
        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            connections.append(client_socket)
            print(f"Accepted connection from {client_address}")
            # Start a new thread to handle the client
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()

    except KeyboardInterrupt:
        print("Server shutting down.")
        # Close all client connections
        for connection in connections:
            connection.close()
        server_socket.close()


def response_all(clients: List[socket.socket], msg):
    while True:
        if msg.not_empty:
            data = msg.get()

            for con in clients:
                try:
                    con.sendall(data)
                except ConnectionError:
                    con.close()
                    clients.remove(con)
                    print(f"Connection with {con} closed")


if __name__ == "__main__":
    main()

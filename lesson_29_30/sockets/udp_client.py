import socket
import threading
from time import sleep

HOST = "localhost"
PORT = 8080
C_PORT = 8085

client_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
client_s.bind((HOST, C_PORT))


def handle_requests():
    while True:
        sleep(0.2)
        msg = input(f"{C_PORT} msg: ").encode()
        client_s.sendto(msg, (HOST, PORT))

        if msg == b"exit":
            sleep(1)
            client_s.shutdown(1)
            client_s.close()
            break


thread = threading.Thread(target=handle_requests, daemon=True)
thread.start()


while True:
    if not thread.is_alive():
        break
    try:
        resp, addr = client_s.recvfrom(1024)

        print(f">>> Response: {resp.decode()}")
        print(f"from {addr}")
    except OSError as e:
        print("connection closed")
        print(e)
        break

import socket
import threading
from time import sleep

HOST = "localhost"
PORT = 8080

client_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
client_s.bind((HOST, 8081))


def handle_responses():
    while True:
        sleep(0.2)
        msg = input("msg: ").encode()
        client_s.sendto(msg, (HOST, PORT))


thread = threading.Thread(target=handle_responses, daemon=True)
thread.start()


while True:
    resp, addr = client_s.recvfrom(1024)
    sleep(0.1)
    print(f">>> Response: {resp.decode()}")
    print(f"from {addr}")
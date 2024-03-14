"""gues the number game server"""

import socket
import random

HOST = "localhost"
PORT = 8080

MSG = b"Well received"
INIT_MSG = b"Send 'Start' to start the game, 'Stop' to end"
GAME_MSG = b"Guess the number 1-10"
WRONG_TYPE_MSG = b"What you sent is not a number"
WIN_MSG = "CONGRATS \U0001F920".encode()
WRONG_NUMBER = b"Try harder"

number = random.randint(1, 10)

server_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_s.bind((HOST, PORT))

print(f"Server is listening on {HOST}: {PORT}")

start_game = False


def receive_msg() -> tuple:
    data, addr = server_s.recvfrom(1024)
    print(f"server received msg from {addr}")
    server_s.sendto(MSG, addr)
    return data.decode(), addr


while True:
    data, addr = receive_msg()

    if data.lower() == "start":
        start_game = True
        server_s.sendto(GAME_MSG, addr)
    elif data.lower() == "stop":
        start_game = False

    while start_game:
        data, addr = receive_msg()
        try:
            if int(data) == number:
                server_s.sendto(WIN_MSG, addr)
                start_game = False
            else:
                server_s.sendto(WRONG_NUMBER, addr)

        except ValueError:
            server_s.sendto(WRONG_TYPE_MSG, addr)
    else:
        server_s.sendto(INIT_MSG, addr)





"""gues the number game server"""

import socket
import random

HOST = "localhost"
PORT = 8080

MSG = b"Well received"
INIT_MSG = "Send 'Start' to start the game or 'Cipher' to start message encryption"
GAME_MSG = b"Guess the number 1-10 or send 'Stop' to end"
GAME_START_MSG = "has started the GAME"
WRONG_TYPE_MSG = "What you sent is not a number"
WIN_MSG = "CONGRATS \U0001F920"
WRONG_NUMBER = b"Try harder"
WELCOME_MSG = "has joined the game"
STOP_MSG = "has stopped the game"

number = random.randint(1, 10)

server_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_s.bind((HOST, PORT))

print(f"Server is listening on {HOST}: {PORT}")

start_game = False
start_encryption = False
users = {"user_count": 0}

user_names = [
    "honey_bunny",
    "lazy_dog",
    "sweet_fury",
    "mr_Bond",
]


def receive_msg() -> tuple:
    try:
        data, addr = server_s.recvfrom(1024)
        print(f"server received msg from {addr}")
        if data != b"exit":
            server_s.sendto(MSG, addr)

        return data.decode(), addr
    except ConnectionResetError:
        return b"exit", None


def play_game():
    print("game started")
    while True:
        print(len(users))
        if len(users) == 1:
            return

        data, addr = receive_msg()

        if data == "exit":
            print(f"exit {users}")
            if addr:
                users.pop(addr)
            continue

        if data.lower() == "stop":
            for a in users:
                if a != "user_count":
                    msg = users[a] + " " + STOP_MSG
                    server_s.sendto(msg.encode(), a)

            return

        if addr not in users:
            users[addr] = user_names[users["user_count"]]
            users["user_count"] += 1
            print(users)
            server_s.sendto(GAME_MSG, addr)
            for a in users:
                if a != "user_count":
                    msg = users[a] + " " + WELCOME_MSG
                    server_s.sendto(msg.encode(), a)

            continue

        try:
            if int(data) == number:
                msg = users[addr] + ", " + WIN_MSG
                for a in users:
                    if a != "user_count":
                        server_s.sendto(msg.encode(), a)

                return
            else:
                server_s.sendto(WRONG_NUMBER, addr)

        except ValueError:
            msg = users[addr] + " " + WRONG_TYPE_MSG
            for a in users:
                if a != "user_count":
                    server_s.sendto(msg.encode(), a)


def procced_encryption(msg: str, salt: int) -> str:
    enc_msg = []
    for i in msg:
        i = chr(ord(i) + salt)
        enc_msg.append(i)

    return "".join(enc_msg)


def encrypt_msg(enc_addr):

    while True:
        server_s.sendto("Send a number to start encryption of the messages".encode(), enc_addr)
        data, addr = receive_msg()

        if addr != enc_addr:
            continue

        try:
            salt = int(data)
            server_s.sendto("number accepted".encode(), addr)
        except ValueError:
            server_s.sendto(WRONG_TYPE_MSG.encode(), addr)
            continue

        break

    while True:
        data, addr = receive_msg()

        if data == "exit":
            print(f"exit {users}")
            if addr:
                for a in users:
                    if a != "user_count":
                        server_s.sendto(f"{users[a]} has left".encode(), a)
                users.pop(addr)

            if addr == enc_addr:
                return

            continue

        if addr == enc_addr:
            data = procced_encryption(data, salt)

        for a in users:
            if a != "user_count":
                server_s.sendto(data.encode(), a)

while True:
    data, addr = receive_msg()

    if data == "exit":
        print(f"exit {users}")
        if addr:
            for a in users:
                if a != "user_count":
                    server_s.sendto(f"{users[a]} has left".encode(), a)
            users.pop(addr)
        continue

    if addr not in users:
        users[addr] = user_names[users["user_count"]]
        users["user_count"] += 1
        print(users)

    if data.lower() == "start":
        start_game = True

    if data.lower() == "cipher":
        start_encryption = True

    if start_game:
        msg = users[addr] + " " + GAME_START_MSG
        print(msg)

        for a in users:
            print(users)
            print(a)

            if a != "user_count":
                server_s.sendto(msg.encode(), a)
                server_s.sendto(GAME_MSG, a)

        play_game()
        start_game = False

    if start_encryption:
        encrypt_msg(addr)
        start_encryption = False

    server_s.sendto(INIT_MSG.encode(), addr)






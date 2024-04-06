import socket
import threading
import time
import json

HOST = "localhost"
PORT = 8080


def print_massage(sck: socket.socket):
    while True:
        try:
            rec = sck.recv(1024)
            recive = json.loads(rec.decode())
            print(f'\r{recive["name"]}: {recive["message"]}')
        except Exception as e:
            print(type(e), e)
        print(">>> ", end="")


with socket.socket() as s:
    s.connect((HOST, PORT))
    name = input("Enter your name: ")
    # name = "TEST"
    receive = threading.Thread(
        target=print_massage,
        args=(s,),
        daemon=True
    )
    receive.start()
    while True:
        # msg = "example"
        msg = input(">>> ")
        if msg == "exit":
            break
        # time.sleep(2)

        massage = {
            "name": name,
            "message": msg
        }
        msg_bites = json.dumps(massage).encode()
        s.sendall(msg_bites)

#    data = s.recv(1024)

# print('Received', repr(data))

#  server is waiting on PORT 8080 !!!
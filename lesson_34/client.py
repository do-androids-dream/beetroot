import socket

HOST = "localhost"
PORT = 8080


client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input(">>> ")
    client.sendall(msg.encode())
    recieve = client.recv(1024)
    print(recieve.decode())

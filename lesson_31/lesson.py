from ssl import wrap_socket as w
import ssl

import requests
import socket

# resp = requests.get("https://api.github.com")
# print(resp.content)
# resp_json = resp.json()
#
# print(resp_json["emojis_url"])

# c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# c_socket.connect(("140.82.121.5", 443))
# ssl_socket = w(c_socket, ssl_version=ssl.PROTOCOL_TLS)
#
# req = b"GET / HTTP/1.1\r\nHost: api.github.com\r\nConnection: close\r\n\r\n"
# resp = []
# ssl_socket.send(req)
# while True:
#     data = ssl_socket.recv(4096)
#     if not data:
#         break
#     resp.append(data)
#
# print(resp)


import ssl
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('github.com', 443))
s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
s.sendall("GET / HTTP/1.1\r\nHost: github.com\r\nConnection: close\r\n\r\n")

while True:

    new = s.recv(4096)
    if not new:
        s.close()
        break
    print(new)

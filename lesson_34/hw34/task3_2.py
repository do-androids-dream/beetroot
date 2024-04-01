"""
Echo server with asyncio

Create a socket echo server which handles each connection using asyncio Tasks.
"""
import socket
import asyncio


HOST = "localhost"
PORT = 8080


async def client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    print(f"CONNECTED {addr}")

    while True:
        request = await reader.read(1024)
        if not request:
            break

        writer.write(request)
        await writer.drain()

    print(f"DISCONNECTED {addr}")
    writer.close()


async def main():
    server = await asyncio.start_server(client, HOST, PORT)
    async with server:
        print(f"SERVER {HOST} : {PORT}")
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())

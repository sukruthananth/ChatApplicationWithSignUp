import socket
import threading
from flask import Flask

FORMAT = 'utf-8'
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def Check_connection(conn, addr):
    print(f"A New Connection {addr} Established")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg ==DISCONNECT_MESSAGE:
                print(f"[Disconnected] {addr}")
                connected = False
            else:
                print(f'{addr} {msg}')
                conn.send("Your message received".encode(FORMAT))


def start():
    server.listen()
    print(f"[Listening] on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=Check_connection, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] Starting server ....")
start()

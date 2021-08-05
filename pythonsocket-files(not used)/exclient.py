import socket
FORMAT = 'utf-8'
HEADER = 64
SERVER = "127.0.0.1"
PORT = 5050
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(ADDR)

def send_message(msg):
    message = msg.encode(FORMAT) # b'How are you doing'
    msg_length = len(message) # 22
    send_len = str(msg_length).encode(FORMAT) # b'22'

    send_len+= b' '* (HEADER - len(send_len)) # b'22

    client_socket.send(send_len)
    client_socket.send(message)
    print(client_socket.recv(2048).decode(FORMAT))

send_message("How are you doing baby")
send_message(DISCONNECT_MESSAGE)
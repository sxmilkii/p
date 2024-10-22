import socket

socket_server = socket.socket()

name = input("Введите своё имя: ")

socket_server.connect(("127.0.0.1", 30))

socket_server.send(name.encode())

socket_name = socket_server.recv(1024).decode()

print(socket_name, "присоединился!")

while True:
    message = socket_server.recv(1024).decode()
    print(socket_name, ":", message)

    message = input("Я: ")
    socket_server.send(message.encode())
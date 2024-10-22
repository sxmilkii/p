import socket

new_socket = socket.socket()

new_socket.bind(("127.0.0.1", 30))

new_socket.listen(3)

print("Сервер запущен!")

name = input("Введите своё имя: ")

conn, addr = new_socket.accept()

client = conn.recv(1024).decode()
print(client + " присоединился!")

conn.send(name.encode()) 

while True:
    message = input("Я: ")
    conn.send(message.encode())

    message = conn.recv(1024).decode()
    print(client, ':', message)
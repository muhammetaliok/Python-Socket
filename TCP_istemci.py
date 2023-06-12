import socket


def connect_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = "Sunucu hop ben geldim"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Gelen veri: {response}")

    client_socket.close()

# Örnek kullanım
server_host = "localhost"
server_port = 12345
connect_server(server_host, server_port)
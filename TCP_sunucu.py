import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Sunucu başlatıldı. İstemci bekleniyor.")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"İstemci bağlandı: {client_address[0]}:{client_address[1]}")
        data = client_socket.recv(1024).decode()
        print(f"Gelen veri: {data}")


        response = "Merhaba"
        client_socket.send(response.encode())
        client_socket.close()

#Example
server_host = "localhost"
server_port = 12345
start_server(server_host, server_port)       
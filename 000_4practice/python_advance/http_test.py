import socket

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 8080))
    server_socket.listen(128)
    client_socket, ip_port = server_socket.accept()
    recv_data = client_socket.recv(4096).decode()
    print(recv_data)
    client_socket.close()
    server_socket.close()

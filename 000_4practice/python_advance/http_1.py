import socket


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('', 8080))
    tcp_server_socket.listen(128)

    service_client_socket, ip_port = tcp_server_socket.accept()
    recv_data = service_client_socket.recv(4096)
    print(recv_data)
    service_client_socket.close()
    tcp_server_socket.close()
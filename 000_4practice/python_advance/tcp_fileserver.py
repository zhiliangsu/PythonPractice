import socket
import os

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 9090))
    server_socket.listen(128)

    while True:
        client_socket, ip_port = server_socket.accept()
        file_name = client_socket.recv(1024).decode()
        print('client info: %s, filename: %s' % (ip_port, file_name))
        if os.path.exists(file_name):
            with open(file_name, 'rb') as file:
                while True:
                    file_data = file.read(1024)
                    if file_data:
                        client_socket.send(file_data)
                    else:
                        break
        else:
            print('File not exists.')
        client_socket.close()
    server_socket.close()
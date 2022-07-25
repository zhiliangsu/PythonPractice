from fileinput import filename
import socket
import os

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.8.176.151', 9090))
    file_name = input('请输入您要下载的文件名：')
    file_name_data = file_name.encode()
    client_socket.send(file_name_data)
    with open('./' + file_name, 'wb') as file:
        while True:
            file_data = client_socket.recv(1024)
            if file_data:
                file.write(file_data)
            else:
                break
    client_socket.close()
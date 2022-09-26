import socket
import os
import threading

def download_file(client_socket, ip_port):

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

def create_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 9090))
    server_socket.listen(128)
    
    while True:
        client_socket, ip_port = server_socket.accept()
        sub_thread = threading.Thread(target=download_file, args=(client_socket, ip_port))
        # download_file(client_socket, ip_port)
        sub_thread.start()
        client_socket.close()
    server_socket.close()

def create_client_socket():
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

def main():
    while True:
        print('='*30)
        print('1.打开文件服务器')
        print('2.下载文件')
        print('3.输入q退出')
        print('='*30)
        choice = input('请输入要操作的功能序号：')

        if choice == '1':
            create_server_socket()
        elif choice == '2':
            create_client_socket()
        elif choice == 'q':
            break
        else:
            print('输入有误，请重新输入...')


if __name__ == '__main__':
    main()
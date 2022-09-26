import socket
import threading


def recv_msg(client_socket, ip_port):
    while True:
        recv_content = client_socket.recv(1024).decode()
        if recv_content:
            print(recv_content)
            client_socket.send('ok，问题正在处理中...').encode()
        else:
            print(ip_port, '客户端断开连接了...')
            break
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 7891))
    server_socket.listen(128)

    while True:
        client_socket, ip_port = server_socket.accept()
        print(ip_port)
        recv_thread = threading.Thread(target=recv_msg, args=(client_socket, ip_port), demon=True)
        recv_thread.start()
    server_socket.close()


if __name__ == '__main__':
    main()
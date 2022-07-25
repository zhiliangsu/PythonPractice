import socket
from urllib import response

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('tlias3.boxuegu.com', 80))

    request_line = 'GET / HTTP/1.1\r\n'
    request_header = 'Host: tlias.boxuegu.com\r\nConnection: close\r\n'
    request_content = request_line + request_header + '\r\n'
    client_socket.send(request_content.encode())

    result = b''
    while True:
        recv_data = client_socket.recv(1024)
        if recv_data:
            result += recv_data
        else:
            break

    # print(result)
    response_list = result.decode().split('\r\n\r\n', 1)
    print(len(response_list))
    print(response_list[1])

    client_socket.close()
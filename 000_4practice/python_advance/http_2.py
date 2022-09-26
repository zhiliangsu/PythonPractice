import socket


if __name__ == '__main__':
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(('www.baidu.com', 80))

    request_line = 'GET / HTTP/1.1\r\n'
    request_header = 'Host: www.baidu.com\r\nConnection:close\r\n'
    request_content = request_line + request_header + '\r\n'
    tcp_client_socket.send(request_content.encode())
    result = b''
    while True:
        recv_data = tcp_client_socket.recv(1024)
        if recv_data:
            result += recv_data
        else:
            break
    print(result)
    response_content = result.decode()
    response_list = response_content.split('\r\n\r\n', 1)
    print(len(response_list))
    print(response_list[1])
    tcp_client_socket.close()
    
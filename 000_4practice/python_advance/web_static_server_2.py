import socket


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 9090))
    tcp_server_socket.listen(128)

    while True:
        service_client_socket, ip_port = tcp_server_socket.accept()
        client_request_data = service_client_socket.recv(4096)
        print(client_request_data)

        with open('static/index.html', 'rb') as file:
            file_data = file.read()

        response_line = 'HTTP/1.1 200 OK\r\n'
        response_header = 'Server: PWS 1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
        response_body = file_data

        response_data = (response_line + response_header + '\r\n').encode() + response_body
        service_client_socket.send(response_data)
        service_client_socket.close()
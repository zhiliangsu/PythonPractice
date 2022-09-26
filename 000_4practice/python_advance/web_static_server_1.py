import socket


tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(('', 9090))
tcp_server_socket.listen(128)

while True:
    service_client_socket, ip_port = tcp_server_socket.accept()
    client_request_data = service_client_socket.recv(4096)
    print(client_request_data)

    response_line = 'HTTP/1.1 200 OK\r\n'
    response_header = 'Server: PWS 1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
    response_body = '<h1>hello world!!!哈哈</h1>'

    response_content = response_line + response_header + '\r\n' + response_body
    service_client_socket.send(response_content.encode())
    service_client_socket.close()
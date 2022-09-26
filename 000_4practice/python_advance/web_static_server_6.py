import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()


class HttpWebServer():
    def __init__(self) -> None:
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(('', 9090))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        while True:
            service_client_socket, ip_port = self.tcp_server_socket.accept()
            gevent.spawn(self.handle_client_request, service_client_socket)

    @staticmethod
    def handle_client_request(service_client_socket):
        client_request_data = service_client_socket.recv(4096)
        print(client_request_data)

        clent_request_content = client_request_data.decode()
        match_obj = re.search(r'/\S*', clent_request_content)
        if not match_obj:
            print('访问路径有误')
            service_client_socket.close()
            return

        resquest_path = match_obj.group()
        print(resquest_path)
        if resquest_path == '/':
            resquest_path = '/index.html'

        try:
            with open('static' + resquest_path, 'rb') as file:
                file_data = file.read()
        except Exception as e:
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            response_header = 'Server: PWS 1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
            response_body = '<h1>非常抱歉，您当前访问的网页已经不存在了</h1>'
            print(e)

            response_data = (response_line + response_header + '\r\n' + response_body).encode()
            service_client_socket.send(response_data)
        else:
            response_line = 'HTTP/1.1 200 OK\r\n'
            response_header = 'Server: PWS 1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
            response_body = file_data

            response_data = (response_line + response_header + '\r\n').encode() + response_body
            service_client_socket.send(response_data)
        finally:
            service_client_socket.close()

def main():
    server = HttpWebServer()
    server.start()


if __name__ == '__main__':
    main()
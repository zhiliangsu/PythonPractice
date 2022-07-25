import socket


if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    udp_socket.sendto('hello world'.encode('utf-8'), ('255.255.255.255', 8080))
    udp_socket.close()
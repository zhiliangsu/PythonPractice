import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local_addr = ('', 7788)
udp_socket.bind(local_addr)

dest_addr = ('10.8.4.158', 8080)
send_data = input('请输入要发送的数据：')

udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
recv_data = udp_socket.recvfrom(1024)
print(recv_data[0].decode('utf-8'))
print(recv_data[1])

udp_socket.close()
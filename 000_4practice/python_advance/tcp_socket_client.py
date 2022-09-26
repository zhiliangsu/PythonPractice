from http import server
import socket

# create socket
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect server
server_ip = input('请输入服务端ip：')
sever_port = int(input('请输入服务端port：'))
tcp_client.connect((server_ip, sever_port))

# send msg
send_data = input('请输入要发送的数据：')
tcp_client.send(send_data.encode())

# recv msg
recv_data = tcp_client.recv(1024)
print('接收到的数据为：', recv_data.decode())

# close socket
tcp_client.close()
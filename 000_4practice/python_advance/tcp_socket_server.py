import socket

# create socket
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind ip and port
tcp_server.bind(('', 7788))

# listen
tcp_server.listen(128)

# accept client connect
client_socket, client_addr = tcp_server.accept()

# recv msg
recv_data = client_socket.recv(1024)
print('接收到的数据为：', recv_data.decode())

# send msg
client_socket.send('thank you!'.encode())

# close client socket
client_socket.close()

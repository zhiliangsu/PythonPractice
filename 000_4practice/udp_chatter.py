import socket


def send_msg(udp_socket):

    msg = input('\n请输入要发送的数据：')
    dst_ip = input('\n请输入对方的ip地址：')
    dst_port = int(input('\n请输入对方的port：'))

    udp_socket.sendto(msg.encode('utf-8'), (dst_ip, dst_port))

def recv_msg(udp_socket):

    recv_data = udp_socket.recvfrom(1024)
    recv_ip = recv_data[1]
    recv_content = recv_data[0].decode('utf-8')

    print('>>>%s:%s' % (str(recv_ip), recv_content))

def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 7890))
    while True:
        print('='*30)
        print('1.发送消息')
        print('2.接收消息')
        print('3.输入q退出')
        print('='*30)
        choice = input('请输入要操作的功能序号：')

        if choice == '1':
            send_msg(udp_socket)
        elif choice == '2':
            recv_msg(udp_socket)
        elif choice == 'q':
            break
        else:
            print('输入有误，请重新输入...')


if __name__ == '__main__':
    main()
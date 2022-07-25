import threading
import time

my_list = list()


def write_data():
    for i in range(5):
        my_list.append(i)
        time.sleep(0.1)
    print('write date:', my_list)

def read_data():
    print('read data:', my_list)


if __name__ == '__main__':
    write_thread = threading.Thread(target=write_data)
    read_thread = threading.Thread(target=read_data)

    write_thread.start()
    # time.sleep(1)
    write_thread.join()
    print('开始读数据了')
    read_thread.start()

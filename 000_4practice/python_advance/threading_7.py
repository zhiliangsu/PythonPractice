import threading
import time

g_num = 0

lock = threading.Lock()

def get_value(index):
    lock.acquire()
    print(threading.current_thread())
    my_list = [2, 4, 6, 8]
    if index >= len(my_list):
        print('下标越界：', index)
        lock.release() # 避免死锁
        return
    value = my_list[index]
    print(value)
    time.sleep(0.2)
    lock.release()


if __name__ == '__main__':
    for i in range(30):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()


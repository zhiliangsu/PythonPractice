import threading

g_num = 0

lock = threading.Lock()

def sum_num1():
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print('sum1:', g_num)
    lock.release()

def sum_num2():
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print('sum2:', g_num)
    lock.release()


if __name__ == '__main__':
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)

    first_thread.start()
    # first_thread.join() # 线程同步
    second_thread.start()

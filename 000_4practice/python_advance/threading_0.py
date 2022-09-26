from time import sleep
import threading

def sing(num):
    print('sing:', threading.current_thread())
    for i in range(num):
        print('正在唱歌...%d' % i)
        sleep(0.2)

def dance(num):
    print('dance:', threading.current_thread())
    for i in range(num):
        print('正在跳舞...%d' % i)
        sleep(0.2)


if __name__ == '__main__':
    print('main:', threading.current_thread())

    thread_list = threading.enumerate()
    print('111:', thread_list, len(thread_list))
    # sing()
    # dance()
    sing_thread = threading.Thread(target=sing, args=(5, ))
    dance_thread = threading.Thread(target=dance, kwargs={'num': 5})

    thread_list = threading.enumerate()
    print('222:', thread_list, len(thread_list))

    sing_thread.start()
    dance_thread.start()

    thread_list = threading.enumerate()
    print('333:', thread_list, len(thread_list))
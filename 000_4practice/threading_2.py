import threading
import time

def show_info():
    for i in range(5):
        print('test:', i)
        time.sleep(0.5)


if __name__ == '__main__':
    
    # sub_thread = threading.Thread(target=show_info) # 主线程会等待所有子线程执行完成后程序再退出
    sub_thread = threading.Thread(target=show_info, daemon=True)
    # 设置为守护主线程，主线程退出后子线程直接销毁，不再执行子线程的代码
    # sub_thread.setDaemon(True)
    sub_thread.start()

    time.sleep(1)
    print('over')
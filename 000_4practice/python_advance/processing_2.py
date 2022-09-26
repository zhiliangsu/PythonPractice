import multiprocessing
import time, os


def work():
    current_process = multiprocessing.current_process()
    print('work:', current_process)
    print('work进程编号:', os.getpid())
    print('work父进程编号:', os.getppid())
    for i in range(10):
        print('工作中....')
        time.sleep(0.2)
        os.kill(os.getpid(), 9)


if __name__ == '__main__':
    current_process = multiprocessing.current_process()
    print('main:', current_process)
    print('main进程的编号:', current_process.pid)

    sub_process = multiprocessing.Process(target=work)
    sub_process.start()
    
    for i in range(20):
        print('我在主进程中执行...')
        time.sleep(0.2)

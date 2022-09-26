import multiprocessing
import time


def run_proc():
    while True:
        print('----2----')
        time.sleep(1)


if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=run_proc)
    sub_process.start()
    while True:
        print('----1----')
        time.sleep(1)

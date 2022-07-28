from inspect import trace
import multiprocessing
import time

my_list = list()

def write_data():
    for i in range(5):
        my_list.append(i)
        time.sleep(0.2)
    print('write_data:', my_list)

def read_data():
    print('read_data:', my_list)


if __name__ == '__main__':
    write_process = multiprocessing.Process(target=write_data)
    read_process = multiprocessing.Process(target=read_data)

    write_process.start()
    write_process.join()
    read_process.start()
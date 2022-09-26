from audioop import mul
import multiprocessing


def show_info(name, age):
    print(name, age)


if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=show_info, name='myprocess',
    args=('古力娜扎', 18))
    sub_process.start()
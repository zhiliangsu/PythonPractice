import imp
import time
import gevent
from gevent import monkey

monkey.patch_all()

def work1(num):
    for i in range(num):
        print('work1...')
        time.sleep(0.2)

def work2(num):
    for i in range(num):
        print('work2...')
        time.sleep(0.2)


if __name__ == '__main__':
    g1 = gevent.spawn(work1, 3)
    g2 = gevent.spawn(work2, 3)

    while True:
        print('主线程中执行')
        time.sleep(0.5)

    # g1.join()
    # g2.join()
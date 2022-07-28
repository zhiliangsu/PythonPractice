import multiprocessing
import time


if __name__ == '__main__':
    queue = multiprocessing.Queue(3)
    queue.put(1)
    queue.put('hello')
    queue.put([3, 5])
    # queue.put((5, 6))
    # queue.put_nowait((5, 6))
    print(queue.full())
    print(queue.empty())
    # time.sleep(0.01)
    if queue.qsize() == 0:
        print('队列为空')
    else:
        print('队列不为空')

    size = queue.qsize()
    print(size)

    value = queue.get()
    print(value)
    size = queue.qsize()
    print(size)

    value = queue.get()
    print(value)
    value = queue.get()
    print(value)
    size = queue.qsize()
    print(size)

    # value = queue.get()
    # print(value)
    # value = queue.get_nowait()
    # print(value)
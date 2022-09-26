import gevent

def work(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

g1 = gevent.spawn(work, 5)
g2 = gevent.spawn(work, 5)
g3 = gevent.spawn(work, 5)
g1.join()
g2.join()
g3.join()
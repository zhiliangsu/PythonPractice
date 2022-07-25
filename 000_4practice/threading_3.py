import threading


class MyThread(threading.Thread):

    def __init__(self, info1, info2):
        super().__init__()
        self.info1 = info1
        self.info2 = info2

    def test1(self):
        print(self.info1)

    def test2(self):
        print(self.info2)

    def run(self):
        self.test1()
        self.test2()


my_thread = MyThread('测试1', '测试2')
my_thread.start()


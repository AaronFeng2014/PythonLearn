"""
python中的多线程


"""

import threading
import time


class PrintNumberThread(threading.Thread):
    __number = 0

    def __init__(self, name, number):
        threading.Thread.__init__(self)
        self.name = name
        self.__number = number

    # 线程中执行的方法
    def printnum(self, threadname, number):
        if threadname == "奇数线程":
            for i in range(number):
                if i % 2 == 0:
                    print(self.name + "%s" % i)
        if threadname == "偶数线程":
            for i in range(number):
                if i % 2 != 0:
                    print(self.name + "%s" % i)

        print("done")

    def run(self):
        self.printnum(self.name, self.__number)


try:

    thread1 = PrintNumberThread("奇数线程", 200)
    thread2 = PrintNumberThread("偶数线程", 200)
    thread1.start()
    thread2.start()
    time.sleep(2)
except:
    print("线程异常")

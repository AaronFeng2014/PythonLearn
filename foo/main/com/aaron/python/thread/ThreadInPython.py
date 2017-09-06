"""
python中的多线程


"""

import _thread


def printNum(threadname, number):
    if threadname == "奇数线程":
        for i in range(number):
            if i % 2 == 0:
                print(i)
    if threadname == "偶数线程":
        for i in range(number):
            if i % 2 != 0:
                print(i)

    print("done")


_thread.start_new_thread(printNum, ("奇数线程", 10))
_thread.start_new_thread(printNum, ("偶数线程", 10))

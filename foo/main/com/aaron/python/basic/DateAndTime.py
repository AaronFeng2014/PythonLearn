"""
Python程序能有很多方式处理日期和时间，转换格式是其中常见的一种方式

Python提供了time和calendar模块来格式化时间和日期

时间间隔是以秒为单位的浮点小数

"""

# 引入time模块
import time

formatTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print(formatTime)
now = time.asctime(time.localtime(time.time()))

print(now)


def now():
    return now("%Y-%m-%d %H:%M:%S")


def now(self, format):
    return time.strftime(format, time.localtime())

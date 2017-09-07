"""
Python程序能有很多方式处理日期和时间，转换格式是其中常见的一种方式

Python提供了time和calendar模块来格式化时间和日期

时间间隔是以秒为单位的浮点小数

"""

# 引入time模块
import time
import calendar

begin = time.clock()
# 时间格式化成字符串
formatTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print(formatTime)
now = time.asctime(time.localtime(time.time()))

print(now)

print(time.localtime(time.time()))


def now():
    return now("%Y-%m-%d %H:%M:%S")


def now(self, format):
    return time.strftime(format, time.localtime())


# 休眠2s
time.sleep(2)

print(calendar.month(2017, 9))

# time.clock()计算上一次调用到本次调用的时间差，用于计算代码执行时间统计
print("time.clock()返回当前的cpu时间，秒数：%s" % (time.clock() - begin))

"""

迭代器是一个可以记住便利位置的对象

迭代器有两个基本的方法： iter()和next()

"""
import sys

ageList = [23, 18, 24, 19, 23]

# 推导式作用于迭代器
ageChange = {age for age in iter(ageList) if age < 20}

print(ageChange)
# 生成迭代器
it = iter(ageList)

print("==============for循环遍历迭代器=================")
for age in it:
    print(age)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

print("==============while循环遍历迭代器=================")
it = iter(ageList)
while True:
    try:
        # next()函数用于从迭代器中获取下一个元素
        print(next(it))
    # 循环退出条件
    except StopIteration:
        print("迭代器已经遍历完成")
        sys.exit()

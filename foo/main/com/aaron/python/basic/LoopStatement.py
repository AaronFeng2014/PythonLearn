"""
Python循环语句解析
    1. while循环
    2. for循环
    3. 嵌套循环
"""

total = 100
print("for循环")
for count in range(1, total):
    if count % 2 == 0:
        print(count)
        if count > 20:
            pass  # 该关键字表示一个占位符，不执行任何操作
            break
    # python根据缩进来确定语句块，语句组的，下面一条语句不属于if的子块，如果在向右缩进4个空格，那么才属于if的子块
    print(count)

print("while循环")
while total:
    print(total)
    total -= 1

ages = [23, 45, 12, 78, 45, 23, 42, 27]

# 修改一个列表中的某个值
ages[2] = 999

del ages[0]
while len(ages) > 0:
    # 从列表尾取出一个元素
    age = ages.pop()
    print(age)

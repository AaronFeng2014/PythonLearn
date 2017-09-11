"""
python中的list结构

    Python中的list是可变的，这是和字符串和元组的最重要的区别

    意思即是：list可修改，而字符串和元组不可修改
"""
# 保存姓名的list
nameList = ["fenghaixin", "ranran", "liyi", "chenyou"]

print(nameList)

# 利用enumerate函数同时遍历列表的索引和值
for index, value in enumerate(nameList):
    print("%s" % index + " : " + value)

# 该方法用于向list尾部添加元素
nameList.append("jiangxing")

print(nameList)

# 修改列表的方式
newNameList = [name + "(test)" for name in nameList]

print("利用zip函数同时遍历多个列表")
for first, second in zip(nameList, newNameList):
    print("%s" % first + " : " + second)

print(newNameList)

# 过滤 + 修改
filterNameList = [name + " ." for name in nameList if name.startswith("h", 4)]
print(filterNameList)

# list的创建方式
print([i for i in range(20)])

# 存放年龄的容器
ageList = [12, 14, 25, 27, 38, 20, 43, 19]

print([age * 2 for age in ageList if age >= 18])

# 从列表中删除元素，指定要删除的初始和结束索引
del ageList[2: 4]

print(ageList)

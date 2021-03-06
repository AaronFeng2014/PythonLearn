"""
Dictionary数据结构：

    类似java中的map结构

"""

dic = {"name": "fenghaixin", "age": 22, "home": "深圳市"}

# dictionary数据结构取值
print(dic["home"])
print(dic["name"])

# 添加，修改Dictionary数据结构中的数据
dic["school"] = "成都大学"

print(dic["school"])
print(dic)

# 字典结构同时遍历key和value
for key, value in dic.items():
    print(key + ":%s " % value)

dic = dict([("area", 23), ("price", 1500), ("cancel", 1)])
print(dic)

# 使用推导式生成字典数据结构
var = {a: a * 2 for a in range(5)}

print(var)

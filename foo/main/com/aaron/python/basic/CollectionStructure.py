"""
Python中的集合数据结构

    集合是一个无序的不重复的元素的集，基本功能有关系测试和消除重复

    可以用{}创建集合，但是创建空的集合要用set{}，而不是{}，因为{}表示创建一个空的字典

"""
# 集合类似于java的set。 自动去重，下面打印语句只会输出17,45,23
ageCollections = {45, 23, 45, 17}

print(ageCollections)

print(89 in ageCollections)
print(45 in ageCollections)
if 45 in ageCollections:
    print("ageCollections中包含45")

# 集合的推导式
newAgeCollections = {age for age in ageCollections if age > 20}
print(newAgeCollections)

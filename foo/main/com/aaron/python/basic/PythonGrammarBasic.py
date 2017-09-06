"""
python包
    1.任何有__init__.py文件的目录都可以作为Python的一个包
    2.import package.module语句引入package包下的module.py文件
        a.该条语句将会在package包下查找__init__.py文件，并执行其顶层的语句
        b.然后查找package包下的module.py文件，并执行文件中所有顶层语句，module.py中的变量，函数和类的定义都可以通过pack.module命名空间获取

"""
from foo.main.com.aaron.python.oo.ClassLearn import Student

"""
python算术运算符
    1. +
    2. -
    3. *
    4. /
    5. **  求幂，如2的10次幂，写作2 ** 10
    6. //  取整除，返回商的整数部分
    7. % 

"""
a = 2
b = 5
print("a * b的值是：")
print(a * b)

"""   
python算术运算符
    1. ==
    2. !=
    3. <> 不等于，用于判断两个对象是否不相等，类似于 != 运算符，在Python 3中已经移除了该运算符了
    4. >
    5. <
    6. >=
    7. <=

"""

"""
python赋值运算符
    1. =
    2. +=
    3. -=
    4. *=
    5. /= 除法赋值运算
    6. %/ 取模赋值运算
    7. **= 幂赋值运算
    8. //=
    
"""
"""
Python逻辑运算符
    1. and  布尔与，如 a and b，当a为false，返回false；否则返回b的计算值
    2. or   布尔或，如 a or b，当a非0，返回a的值，否则返回b的计算值
    3. not  布尔非，如 not a，当a为false，返回true；当a为true，返回false
    

"""
a = True
b = 5

# 短路计算原则，a为false时，整个表达式为false，此时返回a的值，a为true时，计算后续值，即b的值
print(a and b)
print(a or b)
print(not not a)
print(not b)

student = Student("you", "15", "成都市")
print(student._age)
student._study()

# __dict__方法是Python内置的类的属性，包含一个字典，由类的数据属性组成，类似于java中的toString方法
var = Student.__dict__
print(var)

var = Student.__doc__
print(var)

var = Student.__module__
print(var)

var = Student.__bases__
print(var)

var = Student.__name__
print(var)

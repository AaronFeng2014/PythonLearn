"""
Python的面向对象之class

python对象销毁和垃圾回收
    1. Python使用了引用计数器来跟踪对象和垃圾回收，在Python内部记录着每个对象有多少引用，一个内部跟踪变量称之为引用计数器
    2. 当对象被创建，也就创建了一个引用计数器，当引用计数器变为0的时候，该对象可以被垃圾回收，但不是及时回收
    3. 使用引用计数器会涉及到对象之间的循环引用问题，Python的解决方案是同时再使用一个循环垃圾收集器
    4. 析构函数 __del__ 在对象销毁时被调用

"""


class Person:
    # 一个下划线开始，表示protected
    _age = ""

    def __init__(self):
        print("父类构造方法")

    def __del__(self):
        self.study()
        print("Person object is dead")

    def study(self):
        print("人们可以学习" + self)


"""
python类的继承

    1. 在继承中，基类的构造方法 __init__ 不会被自动调用，需要在派生类的构造中显示调用
    2. 在调用基类的方法时，需要加上基类的雷鸣前缀，且需要带上self参数变量，区别在于类中调用过普通函数时不需要带上self参数
    3. Python总是首先找对应类型的方法。如果找不到，则去基类中找

"""


# Student类继承Person类
class Student(Person):
    # 类变量，在类的所有实例之间共享
    __name = "Ran Ran"  # 变量以两个下划线开始，表示私有的，不能从外部访问

    address = ""

    # 这是构造方法，self参数表示类的实例，在定义类方法的时候必须有该参数，但是在方法的调用的时候可以不用传递
    def __init__(self, name, age, address):
        Person.__init__(self)
        self.__name = name
        self._age = age
        self.address = address

        print("子类构造方法")

    # 析构函数，对象销毁的时候调用
    def __del__(self):
        print("Student object is dead")

    def study(self):
        self._eat()
        print("来自" + self.address + "," + self._age + "岁的，" + self.__name + "，开始学习了")

    # 方法以两个下划线开始，表示该方式是私有的
    def _eat(self):
        print("学生除了学习还是要吃饭的")


# 实例化一个类，会调用__init__方法，来初始化参数
student = Student("feng", "23", "成都市")
# student2 = Student("you", "15", "成都市")
student._study()

# print(student.__Student__name)

"""
python中下划线使用规则
    1. 单下划线：
        单下划线开始的变量表示该变量是protected的变量类型，只能被子类或者本类访问
    2. 双下划线：
        表示私有的，只能在类中进行访问
    3. 双尾下划线：
        表示一些特殊的方法，如 __init__  __del__ 方法等
        

"""

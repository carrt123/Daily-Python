"""
1、任何class类在内存里都是一个type类对象
2、python使用type类来创建其他的class。 type（class_name, parents, class_dict)
3、理论上讲，可以使用type来动态创建class
type 继承于object
type（）返回对象类型， 还可以创建类
"""


class Student:
    def greeting(self):
        print("hello")


print(type(Student))  # <class 'type'>
print(isinstance(Student, type))  # True

# 动态创建类, 软件先写， 功能后写
class_body = """
def greeting(self):
    print("hello customer")
"""
class_dict = {}
exec(class_body, globals(), class_dict)  # 将文本转换成字典
Customer = type("Customer", (object,), class_dict)  # 动态创建类

c = Customer()
c.greeting()


"""
装饰器：是一个接受函数作为参数的闭包函数
装饰器的作用：在不改变原函数的代码情况下，给原函数添加额外的功能

闭包：一个闭包是一个函数，以及该函数所引用的任何局部变量， 内部函数引用外部函数的变量， 外部函数然后返回内部函数
"""
from functools import wraps


def decorator(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        print("welcome!")
        result = func(*args, **kwargs)
        return result

    return wrapper


def my_fun1(message: str):
    print(f"I'm ：{message}")


# 使用方法1
f1 = decorator(my_fun1)
f1("jack")


# 使用方法2
@decorator
def my_fun2(message: str):
    print(f"I'm ：{message}")


my_fun2("Jack")

# 更改函数的签名，保持原来的功能， 使用wraps实现
print(my_fun2.__name__)


# wrapper 未添加wraps之前
# my_fun2 添加后


# 支持参数的装饰器
def welcome(name):
    def decorator(func):
        # @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"welcome {name}")
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator

@welcome("张三")
def my_fun3(message: str):
    print(f"I'm {message}")

my_fun3("Jack")
"""
使用类来实现装饰器
"""


class Decorator:
    # 会隐式的把类实例化，并把参数传给__init__方法
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("before")
        result = self.func(*args, **kwargs)
        print("after")
        return result


@Decorator
def hello():
    print("hello")
    return 200


hello()


# 带参数的例子
class ParamDecorator:
    # 但是带了参数后，将不会隐式传入函数
    def __init__(self, name):
        self.name = name

    # 会隐式的把类实例化，并把参数传给__call__方法，执行到hello的时候，扮演装饰器的角色， 用户实际使用的是--call--
    def __call__(self, f):
        def wrap(*args):
            print(f"Hello, {self.name}")
            result = f(*args)
            print(f"Goodby, {self.name}")
            return result

        return wrap


@ParamDecorator("jack")
def hello2():
    print("I'm Bob！")
    return 200


hello2()

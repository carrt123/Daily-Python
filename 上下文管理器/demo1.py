"""
上下文管理器:
    上下文管理器是一个对象，它定义了一个__enter__()方法和一个__exit__()方法。
    上下文管理器对象用于控制被“with”语句封装的代码块的运行。
    在开始执行代码块之前，会调用__enter__()方法；
    在代码块执行完毕后，会调用__exit__()方法。

上下文管理器的作用:
    上下文管理器可以用于管理代码块的运行，例如在代码块运行前和结束后进行一些特定的操作。

使用场景:
    开-关
    锁-释放
    启动-停止
"""

# 常用的现成的上下文管理器: 会自动打开和关闭文件, instance 得到的是--enter--返回的内容， 而不是open("test.txt", "w")
with open("test.txt", "w") as instance:
    instance.write("Hello, World!")

# 自定义一个上下文管理器，计算函数执行时间
import time
class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        return False

    def reset(self):
        self.elapsed = 0


# 使用自定义的上下文管理器
with Timer() as timer:
    nums = []
    for n in range(1000000):
        nums.append(n ** 2)

print(timer.elapsed)

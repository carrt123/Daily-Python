"""
生成器： 生成器是一个可迭代函数，可以挂起保持当前状态。
遇到yield语句返回一个值并保持挂起，遇到next() or send()方法时从当前位置继续执行。

生成器的作用:
1、生成器只有在调用过程才并不会执行全部代码，比列表推导式更省内存， 性能高
2、简化代码, 比迭代器方便

"""


def hello():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3


# 使用方法1
g = hello() #首先实例化
print(next(g))
print(next(g))
print(next(g))


# 使用方法2
g = hello()
for res in g:
    print(res)


# 定义一个得到平方数的生成器
def square(count):
    for n in range(count):
        yield n**2


for num in square(5):
    print(num)
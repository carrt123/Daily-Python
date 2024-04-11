"""
built-in 范围最大 :内置数据
model 范围第二大 : .py文件
本地范围 范围最小 ：函数内部
python 动态语言， 在运行时确定变量类型

查找数据的顺序： 本地-》 model -》built
"""

count = 10
print(count)


def func(flag: bool):
    if flag:
        count = 100
    print(count)


"""
两个count并不是同一个， 如何修改func的count值， 外面的count不受影响。

如果想修改的外面的值， 可以使用global关键字
"""

func(True)  # 10 100
#func(False) # 报错
"""
解释: python 分为编译和运行两个过程
在编译时， 并不知道 if flag下的内容是否执行，
在执行时， 才根据if flag的值来执行， 此时本地count还没有被赋值， 由于先找本地范围，所以报错
"""
print('--------------')
ans = 15
print(ans)
def func2():
    ans = 10
    print(ans)

func2()
print(ans)  # 15 10 15

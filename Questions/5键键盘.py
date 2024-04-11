matrix = list(map(int, input().split()))


def getResult(matrix):
    clip = []
    screen = []
    isSelect = False

    for command in matrix:
        if command == 1:
            if isSelect:
                screen.clear()
            screen.append('a')
            isSelect = False

        elif command == 2:
            if isSelect:
                clip.clear()
                clip.extend(screen)

        elif command == 3:
            if isSelect:
                clip.clear()
                clip.extend(screen)
                screen.clear()
            isSelect = False

        elif command == 4:
            if isSelect:
                screen.clear()
            screen.extend(clip)
            isSelect = False

        elif command == 5:
            if len(screen) != 0:
                isSelect = True

    return len(screen)


print(getResult(matrix))

#
# 题目描述
# 有一个特殊的5键键盘，上面有a，ctrl-c，ctrl-x，ctrl-v，ctrl-a五个键。
#
# a键在屏幕上输出一个字母a；
#
# ctrl-c将当前选择的字母复制到剪贴板；
#
# ctrl-x将当前选择的字母复制到剪贴板，并清空选择的字母；
#
# ctrl-v将当前剪贴板里的字母输出到屏幕；
#
# ctrl-a选择当前屏幕上的所有字母。
#
# 注意：
#
# 剪贴板初始为空，新的内容被复制到剪贴板时会覆盖原来的内容
# 当屏幕上没有字母时，ctrl-a无效
# 当没有选择字母时，ctrl-c和ctrl-x无效
# 当有字母被选择时，a和ctrl-v这两个有输出功能的键会先清空选择的字母，再进行输出
# 给定一系列键盘输入，输出最终屏幕上字母的数量。
#
# 输入描述
# 输入为一行，为简化解析，用数字1 2 3 4 5代表a，ctrl-c，ctrl-x，ctrl-v，ctrl-a五个键的输入，数字用空格分隔。
# 输出描述
# 输出一个数字，为最终屏幕上字母的数量。
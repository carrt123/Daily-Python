import re

s = input()
temp = re.compile(r"A=\{(.+)},B=\{(.+)},R=(.+)").search(s)
A = list(map(int, temp.group(1).split(',')))
B = list(map(int, temp.group(2).split(',')))
R = int(temp.group(3))


def getResult():
    res = []
    ant = 0
    for a in A:
        for b in B:
            if a > b:
                continue
            if (b - a) <= R or ant == 0:
                res.append(f"({a},{b})")
                ant += 1
            else:
                break
    return "".join(res)


print(getResult())

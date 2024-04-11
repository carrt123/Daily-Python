class UnionFindSet:

    def __init__(self, n: int):
        self.fa = [i for i in range(n)]
        self.count = n

    def find(self, x: int):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]
        return x

    def union(self, x: int, y: int):
        x_fa = self.find(x)
        y_fa = self.find(y)

        if x_fa != y_fa:
            self.fa[y_fa] = x_fa

    def getCount(self):
        return self.count


n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

# 段代码的作用是将输入的一行字符串按空格分割成多个字符串，然后将这些字符串转换为整数类型。让我举个例子来说明：
# 假设输入的一行字符串是 "3 4 5"，经过 input().split() 操作后，得到的字符串列表是 ["3","4","5"]，
# 然后经过 map(int,...) 操作，将这些字符串转换为整数类型，最终得到整数列表 [3,4,5]。

ufs = UnionFindSet(n)
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] == 1:
            ufs.union(i, j)

connected = {}

for i in range(n):
    fa = ufs.find(ufs.fa[i])
    connected[fa] = connected.get(fa, 0) + 1

print(max(connected.values()))

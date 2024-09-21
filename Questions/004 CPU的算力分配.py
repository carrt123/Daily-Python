def getResult():
    a, b = map(int, input().split())

    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_set = set()
    b_set = set()
    a_sum = 0
    b_sum = 0
    ans = 0
    for x in a_list:
        a_sum += x
        a_set.add(x)
    for y in b_list:
        b_sum += y
        b_set.add(y)
    min_a = 0xffff
    for x in a_list:
        target = (b_sum - a_sum + 2 * x) // 2
        if target in b_set and x < min_a:
            ans = f"{x} {target}"
            min_a = x
    return ans


while True:
    print(getResult())

import math

def dp(x):
    if x == 1:
        print("0")
        return
    if x == 2:
        print("1")
        return

    d = [0] * (n + 1)
    d[2] = 1
    d[3] = 1
    for i in range(4, n+1):
        one, two, three = math.inf, math.inf, d[i-1]
        if i % 2 == 0:
            one = d[i // 2]
        if i % 3 == 0:
            two = d[i // 3]
        d[i] = 1 + min(one, two, three)
    print(d[n])

n = int(input())
dp(n)
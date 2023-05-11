n, m = map(int, input().split())

ch=[0]*(m+1)
for i in range(2, m+1):
    if ch[i] == 0:
        if i >= n and i <= m:
            print(i)
        for j in range(i, m+1, i):
            ch[j] = 1
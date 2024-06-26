import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i


def find(k):
    if k == parent[k]:
        return k
    else:
        p = find(parent[k])
        parent[k] = p
        return parent[k]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    x, a, b = map(int, sys.stdin.readline().split())
    if x == 0:
        union(a, b)
    elif x == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
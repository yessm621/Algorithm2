import sys

n = int(input())
data = []
for _ in range(n):
    data.append(sys.stdin.readline().strip())
data = list(set(data))

data.sort()
data.sort(key = len)
for d in data:
    print(d)
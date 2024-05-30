import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        arr.pop()
        continue
    arr.append(x)

print(sum(arr))
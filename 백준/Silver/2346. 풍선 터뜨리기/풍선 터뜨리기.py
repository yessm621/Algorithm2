import sys
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = deque()
for i in range(n):
    arr2.append((i+1, arr[i]))

result = []
while arr2:
    idx, a = arr2.popleft()
    result.append(idx)

    if a > 0:
        arr2.rotate(-(a-1))
    else:
        arr2.rotate(-a)
print(*result, sep=' ')
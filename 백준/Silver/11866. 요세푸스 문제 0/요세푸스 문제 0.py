import sys

from collections import deque
n, k = map(int, sys.stdin.readline().split())

arr = deque()
for i in range(1, n+1):
    arr.append(i)

result = []
while arr:
    arr.rotate(-k+1)
    result.append(arr.popleft())

print("<", end='')
print(', '.join(map(str, result)), end='')
print(">", end='')
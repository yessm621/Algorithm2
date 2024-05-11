import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
arr = [0]
temp = 0
for i in a:
    temp += i
    arr.append(temp)

for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])
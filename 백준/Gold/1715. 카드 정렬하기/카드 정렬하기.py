import sys
import heapq

n = int(input())
a = []
for _ in range(n):
    heapq.heappush(a, int(input()))

result = 0
if len(a) == 1:
    print(result)
else:
    for i in range(n-1):
        p = heapq.heappop(a)
        c = heapq.heappop(a)

        result += (p + c)
        heapq.heappush(a, p + c)
    print(result)
from collections import Counter

n = int(input())
a = list(map(int, input().split()))
a_cnt = Counter(a)

result = [-1] * n
stack = []
stack.append(0)
for i in range(1, n):
    while stack and a_cnt[a[stack[-1]]] < a_cnt[a[i]]:
        result[stack.pop()] = a[i]
    stack.append(i)
print(*result)
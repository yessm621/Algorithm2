import sys

n = int(sys.stdin.readline())
plus = []
minus = []
result = 0
for _ in range(n):
    m = int(sys.stdin.readline())
    if m > 1:
        plus.append(m)
    elif m <= 0:
        minus.append(m)
    else:
        result += m

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i + 1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2):
    if i + 1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])

print(result)
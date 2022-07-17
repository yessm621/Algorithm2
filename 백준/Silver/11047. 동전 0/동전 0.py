n, k = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
money.sort(reverse=True)

result = 0
for m in money:
    if k == 0:
        break
    if k // m > 0:
        result += k // m
        k -= (k // m) * m

print(result)
n, m = map(int, input().split())
basket = [0] * n
for i in range(n):
    basket[i] = i+1

for _ in range(m):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for b in basket:
    print(b, end = ' ')
n, m = map(int, input().split())
a = list(range(1,n+1))

for _ in range(m):
    i, j, k = map(int, input().split())
    a[i-1:j] = a[k-1:j] + a[i-1:k-1]
for x in a:
    print(x, end = ' ')
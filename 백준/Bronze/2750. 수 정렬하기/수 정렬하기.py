n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

for d in data:
    print(d)
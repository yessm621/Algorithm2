n = int(input())
data = list(map(int, input().split()))
data_set = set(data)
a = list(data_set)
a.sort()

result = {}
for i in range(len(a)):
    result[a[i]] = i

for d in data:
    print(result[d], end = ' ')
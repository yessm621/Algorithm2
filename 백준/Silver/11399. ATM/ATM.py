N = int(input())
people = list(map(int, input().split()))

people.sort()
result = 0
tmp = 0
for i in range(N):
    tmp += people[i]
    result += tmp
print(result)
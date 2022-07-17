n = int(input())
room = []
for _ in range(n):
    s, e = map(int, input().split())
    room.append((s, e))
room.sort(key = lambda x:(x[1], x[0]))

et = 0
result = 0
for s, e in room:
    if s >= et:
        et = e
        result += 1
print(result)
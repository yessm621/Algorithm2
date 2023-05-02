n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

stack = []
result = []
i = 0
cnt = 1
while i < n:
    if not stack:
        stack.append(cnt)
        result.append('+')
        cnt += 1
        continue
    
    if stack[-1] == data[i]:
        stack.pop()
        result.append('-')
        i += 1
    elif stack[-1] < data[i]:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    else:
        result = []
        break

if result:
    for r in result:
        print(r)
else:
    print("NO")

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

stack = []
cnt = 1
for a in arr:
    stack.append(a)

    while stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1

if stack:
    print("Sad")
else:
    print("Nice")
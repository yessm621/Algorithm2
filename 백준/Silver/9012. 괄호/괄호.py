import sys

n = int(sys.stdin.readline())
for _ in range(n):
    arr = list(sys.stdin.readline().rstrip())
    stack = []
    for a in arr:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(a)
            else:
                stack.append(a)

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
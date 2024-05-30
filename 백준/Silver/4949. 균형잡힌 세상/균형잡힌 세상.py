import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == '.':
        break
    syntax = list(n)
    stack = []
    for s in syntax:
        if s.isalpha():
           continue

        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)
        elif s == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
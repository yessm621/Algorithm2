import sys

n = int(input())
stack = []
for _ in range(n):
    command = sys.stdin.readline()
    text = command.split()[0]
    if text == 'push':
        stack.append(command.split()[1])
    elif text == 'pop':
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif text == 'size':
        print(len(stack))
    elif text == 'top':
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
        
    elif text == 'empty':
        if len(stack) == 0:
            print("1")
        else:
            print("0")
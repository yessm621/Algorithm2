import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    cmd = sys.stdin.readline().split()    
    cmd[0] = int(cmd[0])
    if cmd[0] == 1:
        stack.append(cmd[1])
    elif cmd[0] == 2:
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif cmd[0] == 3:
        print(len(stack))
    elif cmd[0] == 4:
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif cmd[0] == 5:
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
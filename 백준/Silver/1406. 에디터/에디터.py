import sys

data = list(input())
n = int(input())

tmp = []
for _ in range(n):
    command = (sys.stdin.readline().rstrip()).split()
    if command[0] == 'L':
        if data:
            tmp.append(data.pop())
    elif command[0] == 'D':
        if tmp:
            data.append(tmp.pop())
    elif command[0] == 'B':
        if data:
            data.pop()
    elif command[0] == 'P':
        data.append(command[1])
    
data.extend(reversed(tmp))
print(''.join(data))
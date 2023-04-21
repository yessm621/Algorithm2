n, b = map(int, input().split())
tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = ''
while n != 0:
    answer += str(tmp[n % b])
    n = n // b
print(answer[::-1])
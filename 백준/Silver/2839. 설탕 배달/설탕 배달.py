N = int(input())
types = [5, 3]

count = 0
num = N // 5
for n in range(num, 0, -1):
    count = 0
    tmp = N
    tmp -= 5 * n
    if tmp % 3 == 0:
        count = n
        count += tmp // 3
        break
    else:
        continue

num = N // 3
for n in range(num, 0, -1):
    tmp = N
    if tmp % 3 == 0:
        if count == 0 or (tmp // 3 < count):
            count = tmp // 3
        break
    else:
        if count == 0:
            count = -1
print(count)
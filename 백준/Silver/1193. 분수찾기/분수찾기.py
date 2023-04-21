n = int(input())


s = 2
e = 3
i = 3
while True:
    if n == 1:
        print('1/1')
        break
    if s <= n and n <= e:
        if (i-1) % 2 == 0:
            x = n - s
            print(1+x, '/', i-1-x, sep='')
        else:
            x = n - s
            print(i-1-x,'/',1+x, sep='')
        break
    s = e + 1
    e = e + i
    i += 1
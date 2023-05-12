t = int(input())
for _ in range(t):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    x = tmp[1:]
    
    result = 0
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            a, b = x[i], x[j]
            while b != 0:
                a, b = b, a % b
            result += a
    print(result)
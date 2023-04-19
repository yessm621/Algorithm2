n = int(input())
for _ in range(n):
    tmp = list(map(int, input().split()))
    k = tmp[0]
    score = tmp[1:]
    avg = sum(score) // k
    
    cnt = 0
    for s in score:
        if s > avg:
            cnt += 1
    print("{:.3f}%".format((cnt/k)*100))
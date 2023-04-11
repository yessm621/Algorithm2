n, m = map(int, input().split())
a = list(map(int, input().split()))

def Count(mid):
    cnt = 1
    s = 0
    for x in a:
        if s + x > mid:
            cnt += 1
            s = x
        else:
            s += x
    return cnt

lt = 0
rt = sum(a)
result = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) <= m:
        result = mid
        rt = mid - 1
    else:
        lt = mid + 1
if result < max(a):
    result = max(a)
print(result)
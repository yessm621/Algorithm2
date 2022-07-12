n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

lt = 0
rt = tree[n-1]
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    sum = 0
    for t in tree:
        if t - mid > 0:
            sum += (t - mid)
        if sum > m:
            break
    if sum > m:
        res = mid
        lt = mid + 1
    elif sum < m:
        rt = mid - 1
    else:
        res = mid
        break

print(res)
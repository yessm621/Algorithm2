import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))

def check(arr):
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

        cnt = 1
        for j in range(n-1):
            if arr[j][i] == arr[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    return max_cnt


result = 0
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            cnt = check(arr)
            result = max(result, cnt)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        if i + 1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            cnt = check(arr)
            result = max(result, cnt)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(result)
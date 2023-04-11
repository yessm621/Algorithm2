n = int(input())
a = list(map(int, input().split()))
arr = {}
for x in a:
    if x in arr:
        arr[x] += 1
    else:
        arr[x] = 1

m = int(input())
b = list(map(int, input().split()))

result = []
for x in b:
    try:
        print(arr[x], end = ' ')
    except:
        print(0, end = ' ')
n = int(input())
a =list(map(int, input().split()))
a.sort()

count = 0
for k in range(0, n):
    i = 0
    j = n - 1
    while i < j:
        if a[i] + a[j] > a[k]:
            j -= 1
        elif a[i] + a[j] < a[k]:
            i += 1
        elif a[i] + a[j] == a[k]:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
print(count)
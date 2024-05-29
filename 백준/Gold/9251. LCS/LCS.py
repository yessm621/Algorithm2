import sys

str1 = [0] + list(sys.stdin.readline().rstrip())
str2 = [0] + list(sys.stdin.readline().rstrip())
len1 = len(str1)
len2 = len(str2)

arr = [[0 for _ in range(len1)] for _ in range(len2)]
for i in range(1, len2):
    for j in range(1, len1):
        if str2[i] == str1[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(arr[-1][-1])
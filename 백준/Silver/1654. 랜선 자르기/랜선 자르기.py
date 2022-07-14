k, n = map(int, input().split())

line = []
for _ in range(k):
	line.append(int(input()))

lt = 1
rt = max(line)
result = 0
while lt <= rt:

	cnt = 0
	mid = (lt + rt) // 2

	for l in line:
		cnt += l // mid
	
	if cnt >= n:
		result = mid
		lt = mid + 1
	else:
		rt = mid - 1
print(result)
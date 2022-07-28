k = int(input())
rope = []
for _ in range(k):
	rope.append(int(input()))
rope.sort(reverse=True)	

result = 0
for i in range(k):
	temp = (i+1) * rope[i]
	if result < temp:
		result = temp

print(result)
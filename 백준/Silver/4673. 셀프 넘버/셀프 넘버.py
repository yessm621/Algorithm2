numbers = [0] * 10001

def d(n):
	data = n
	for x in str(n):
		data += int(x)

	if data <= 10000:
		numbers[data] = 1
		d(data)
	

n = 1
while n <= 10000:
	if numbers[n] == 0:
		d(n)
	n += 1

for i in range(1, 10001):
	if numbers[i] == 0:
		print(i)
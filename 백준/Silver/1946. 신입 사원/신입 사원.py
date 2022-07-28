import sys

t = int(input())

for _ in range(t):
	count = 1
	n = int(input())
	people = []
	for _ in range(n):
		a, b = map(int, sys.stdin.readline().split())
		people.append([a, b])
	people.sort()

	Max = people[0][1]
	for i in range(n):
		if Max > people[i][1]:
			Max = people[i][1]
			count += 1

	print(count)
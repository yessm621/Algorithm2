import re
number = input()
numbers = re.split(r'\+|\-', number)
arithmetic_pattern = re.compile(r'\D')
arithmetic = re.findall(arithmetic_pattern, number)

if not arithmetic:
	print(int(numbers[0]))
else:
	length = len(arithmetic)
	for i in range(0, length-1):
		if arithmetic[i] == '-':
			if arithmetic[i+1] == '+':
				arithmetic[i+1] = '-'

	result = int(numbers[0])
	for i in range(0, length):
		if arithmetic[i] == '-':
			result -= int(numbers[i+1])
		else:
			result += int(numbers[i+1])
	print(result)
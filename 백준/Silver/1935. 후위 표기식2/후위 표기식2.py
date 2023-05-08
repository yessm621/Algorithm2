n = int(input())
s = list(input())

v = []
for _ in range(n):
    v.append(int(input()))

stack = []
for x in s:
    if x.isalpha():
        stack.append(v[ord(x) - ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if x == '+':
            stack.append(str1+str2)
        elif x == '-':
            stack.append(str1-str2)
        elif x == '*':
            stack.append(str1*str2)
        elif x == '/':
            stack.append(str1/str2)
print("%.2f" % stack[0])
s = input()
d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0
for i in range(len(s)):
    for j in d:
        if s[i] in j:
            result += d.index(j) + 3
print(result)
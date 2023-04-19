s = input()
data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for d in data:
    s = s.replace(d, '*')
print(len(s))
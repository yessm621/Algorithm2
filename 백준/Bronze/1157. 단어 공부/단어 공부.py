s = input().upper()
data = {}
for x in s:
    if x in data:
        data[x] += 1
    else:
        data[x] = 1

tmp = [k for k,v in data.items() if max(data.values()) == v]
if len(tmp) > 1:
    print("?")
else:
    print(tmp[0])
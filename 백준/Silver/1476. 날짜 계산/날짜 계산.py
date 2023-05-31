e, s, m = map(int, input().split())

result = ee = ss = mm = 1
while True:
    if e == ee and s == ss and m == mm:
        break
    result += 1
    ee += 1
    ss += 1
    mm += 1

    if ee > 15: ee = 1
    if ss > 28: ss = 1
    if mm > 19: mm = 1

print(result)
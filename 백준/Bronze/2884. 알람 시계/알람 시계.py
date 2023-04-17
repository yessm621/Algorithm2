h, m = map(int, input().split())

result_h = 0
result_m = 0
if m - 45 >= 0:
    result_m = m - 45
else:
    result_h = 1
    result_m = 60 + (m - 45)
if h - result_h >= 0:
    result_h = h - result_h
else:
    result_h = 24 + (h - result_h)
print(result_h, result_m)
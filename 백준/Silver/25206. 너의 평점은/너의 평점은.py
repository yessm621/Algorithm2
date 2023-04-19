t = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

sum1 = 0.0
sum2 = 0.0
for _ in range(20):
    name, score, grade = input().split()
    if grade in t:
        sum1 += float(score) * t[grade]
        sum2 += float(score)

print("{:.6f}".format(sum1/sum2))
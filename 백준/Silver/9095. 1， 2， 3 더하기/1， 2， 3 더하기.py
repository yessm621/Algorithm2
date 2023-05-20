t = int(input())
def combi(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return combi(n-1) + combi(n-2) + combi(n-3)

for _ in range(t):
    n = int(input())
    print(combi(n))
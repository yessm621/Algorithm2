def number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

n, m = map(int, input().split())

five_count = number(n, 5) - number(m, 5) - number(n - m, 5)
two_count = number(n, 2) - number(m, 2) - number(n - m, 2)

print(min(five_count, two_count))
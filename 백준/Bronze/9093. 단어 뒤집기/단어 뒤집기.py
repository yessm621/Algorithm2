n = int(input())
for _ in range(n):
    text = input()
    arr_t = list(text.split(' '))
    for t in arr_t:
        x = list(t)
        x.reverse()
        x = ''.join(x)
        print(x, end = ' ')
    print()
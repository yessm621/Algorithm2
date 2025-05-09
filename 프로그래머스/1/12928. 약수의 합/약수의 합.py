def solution(n):
    answer = 0
    if n == 0 or n == 1:
        return n
    for i in range(1, (n + 1) // 2):
        if n % i == 0:
            k = n // i
            if k < i:
                break
            answer += i
            if k != i:
                answer += (n // i)
    return answer
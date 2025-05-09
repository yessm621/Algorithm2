def solution(n):
    answer = 0

    val = str(n)
    for v in val:
        answer += int(v)

    return answer
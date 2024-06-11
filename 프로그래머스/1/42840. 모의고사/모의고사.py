def solution(answers):
    answer = [0 for i in range(3)]
    
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            answer[0] += 1
        if answers[i] == b[i%len(b)]:
            answer[1] += 1
        if answers[i] == c[i%len(c)]:
            answer[2] += 1
    
    result = []
    for i in range(len(answer)):
        if answer[i] == max(answer):
            result.append(i+1)
    
    return sorted(result)
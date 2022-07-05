def solution(n, computers):
    answer = n
    path = []
    
    if n == 1:
        return 1
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j]:
                if path.count(i) < 1:
                    path.append(i)
                if path.count(j) < 1:
                    path.append(j)
                    
    if len(path) == 0:
        return n
    return answer - len(set(path)) + 1
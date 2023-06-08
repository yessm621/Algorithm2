def solution(priorities, location):
    q = [(i,p) for i,p in enumerate(priorities)]
    
    answer = 0
    result = []
    while True:
        cur = q.pop(0)
        if any(cur[1] < x[1] for x in q):
            q.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

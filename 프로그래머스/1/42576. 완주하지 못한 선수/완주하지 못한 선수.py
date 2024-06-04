def solution(participant, completion):
    answer = ''
    data = {}
    for p in participant:
        if data.get(p):
            data[p] += 1
        else:
            data[p] = 1
    
    comple = {}
    for c in completion:
        if comple.get(c):
            comple[c] += 1
        else:
            comple[c] = 1

    for d in data:
        if d in comple:
            data[d] -= comple[d]
    
    for d in data:
        if data.get(d) == 1:
            answer = d
            break
    
    return answer
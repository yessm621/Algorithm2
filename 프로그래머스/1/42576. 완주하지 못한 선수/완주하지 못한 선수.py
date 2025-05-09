def solution(participant, completion):
    answer = ''
    data = {}
    for p in participant:
        data[p] = data.get(p, 0) + 1
    
    for c in completion:
        data[c] -= 1
    
    for k, v in data.items():
        if v > 0:
            answer = k
            break
    
    return answer
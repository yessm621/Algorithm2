def solution(participant, completion):
    data = {}
    for p in participant:
        data[p] = data.get(p, 0) + 1
    
    for c in completion:
        data[c] -= 1
    
    answer = [k for k, v in data.items() if v > 0][0]
    
    return answer
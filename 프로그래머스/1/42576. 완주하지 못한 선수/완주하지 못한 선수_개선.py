def solution(participant, completion):
    answer = ''
    data = {}
    for p in participant:
        # get(key, x): 딕셔너리에 key값이 있으면 key 값에 해당하는 value를 반환, 없으면 x를 반환함.
        data[p] = data.get(p, 0) + 1
    
    for c in completion:
        data[c] -= 1

    # items()를 사용해 key, value로 동시 조회
    for k, v in data.items():
        if v > 0:
            answer = k
            break
    
    return answer

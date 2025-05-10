def solution(clothes):
    answer = 1
    data = {}
    for clothe in clothes:
        data[clothe[1]] = data.get(clothe[1], 0) + 1
    
    for k, v in data.items():
        answer *= (v + 1)
    
    return answer - 1
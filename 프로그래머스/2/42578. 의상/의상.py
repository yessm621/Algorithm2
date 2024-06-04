def solution(clothes):
    d = {}
    for name, key in clothes:
        if d.get(key):
            d[key] += [name]
        else:
            d[key] = [name]
    
    answer = 1
    for key, value in d.items():
        answer *= (len(value) + 1)
    
    return answer - 1
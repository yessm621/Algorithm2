def solution(s):
    answer = ''
    result = s.split(" ")
    
    result = list(map(int, result))
    
    i = max(result)
    j = min(result)
    
    answer = str(j) + " " + str(i)
    return answer
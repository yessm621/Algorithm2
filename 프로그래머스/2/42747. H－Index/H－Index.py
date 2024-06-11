def solution(citations):
    answer = 0
    
    lt = 0
    rt = max(citations)
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 0
        for c in citations:
            if c >= mid:
                cnt += 1
        
        if cnt >= mid:
            answer = mid
            lt += 1
        else:
            rt -= 1
    
    return answer

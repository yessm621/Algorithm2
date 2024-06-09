from collections import deque

def solution(priorities, location):
    answer = 0
    arr = deque()
    for i in range(len(priorities)):
        arr.append((i, priorities[i]))
    
    while arr:
        check = False
        tmp = arr.popleft()
        
        for a in arr:
            if tmp[1] < a[1]:
                arr.append(tmp)
                check = True
                break
        if not check:
            answer += 1
            if tmp[0] == location:
                break
    
    return answer
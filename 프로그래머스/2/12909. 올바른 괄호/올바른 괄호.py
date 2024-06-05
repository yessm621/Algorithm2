def solution(s):
    answer = True
    arr = list(s)
    
    stack = []
    for a in arr:
        if a == '(':
            stack.append(a)
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(a)
            else:
                stack.append(a)
                break
    
    if stack:
        answer = False
    
    return answer
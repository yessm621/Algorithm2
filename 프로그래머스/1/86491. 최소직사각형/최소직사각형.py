def solution(sizes):
    answer = 0
    max_x = 0
    max_y = 0
    for i in range(len(sizes)):
        x = sizes[i][0]
        y = sizes[i][1]
        if x < y:
            tmp = x
            x = y
            y = tmp
        sizes[i][0] = x
        sizes[i][1] = y
        
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
            
    return max_x * max_y
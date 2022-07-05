answer = 0

def solution(numbers, target):
    check = [0] * len(numbers)
    
    def DFS(L):
        if L == len(numbers):
            count = 0
            for i in range(len(check)):
                if check[i] == 1:
                    count += numbers[i]
                else:
                    count -= numbers[i]
            if count == target:
                global answer
                answer += 1
        else:
            check[L] = 1
            DFS(L+1)
            check[L] = 0
            DFS(L+1)
    DFS(0)
    return answer
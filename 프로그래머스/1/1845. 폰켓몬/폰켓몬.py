def solution(nums):
    data = {}
    for n in nums:
        if data.get(n):
            data[n] += 1
        else:
            data[n] = 1
    
    answer = len(nums) // 2
    if answer > len(data):
        answer = len(data)
    
    return answer
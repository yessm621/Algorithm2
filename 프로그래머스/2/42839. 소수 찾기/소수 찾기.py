import itertools

def isPrime(x):
    if x <= 1:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
        

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    
    tmp = []
    for i in range(1, len(numbers) + 1):
        tmp += list(itertools.permutations(numbers, i))
        
    nums = [int(''.join(t)) for t in tmp]
    nums = list(set(nums))
    
    for n in nums:
        if isPrime(n):
            answer += 1

    return answer
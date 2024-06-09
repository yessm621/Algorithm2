from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    b = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    w = 0
    while len(truck_weights) != 0:
        time += 1
        w -= b.popleft()
        
        if w + truck_weights[0] <= weight:
            w += truck_weights[0]
            b.append(truck_weights.popleft())
        else:
            b.append(0)
            
    time += bridge_length
    
    return time
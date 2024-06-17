from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    stack = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    w = 0
    while truck_weights:
        time += 1
        w -= stack.popleft()
        
        if w + truck_weights[0] <= weight:
            w += truck_weights[0]
            stack.append(truck_weights.popleft())
        else:
            stack.append(0)

    return time + bridge_length
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=[0 for _ in range(bridge_length)]
    w=0
    while bridge:
        answer+=1
        x=bridge.pop(0)
        if x!=0:
            w-=x
        if truck_weights:
            if w+truck_weights[0]<=weight:
                t=truck_weights.pop(0)
                bridge.append(t)
                w+=t
            else:
                bridge.append(0)
    return answer
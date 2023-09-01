from collections import deque
def solution(priorities, location):
    answer = 0
    q=deque()
    s=1
    for i in range(len(priorities)):
        q.append((priorities[i],i))
    while (q):
        x=q.popleft()
        if x[0]==max(priorities):
            if x[1]==location:
                answer=s
                break
            else:
                s+=1
                priorities[x[1]]=-1
        else:
            q.append(x)
    return answer
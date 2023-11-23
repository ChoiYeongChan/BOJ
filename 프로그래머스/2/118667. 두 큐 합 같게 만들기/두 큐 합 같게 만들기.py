from collections import deque
def solution(queue1, queue2):
    answer = 0
    tot1=sum(queue1)
    tot2=sum(queue2)
    total=tot1+tot2
    limit=len(queue1)*4
    queue1=deque(queue1)
    queue2=deque(queue2)
    while True:
        if tot1==tot2:
            break
        elif tot1>tot2:
            t=queue1.popleft()
            queue2.append(t)
            tot1-=t
            tot2+=t
            answer+=1
        else:
            t=queue2.popleft()
            queue1.append(t)
            tot2-=t
            tot1+=t
            answer+=1
        if answer==limit:
            answer=-1
            break
    return answer
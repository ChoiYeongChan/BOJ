import sys
from collections import deque
a,b=map(int,sys.stdin.readline().split())
queue=deque()
for i in range(1,a+1):
    queue.append(i)
print('<',end='')
cnt=0
while queue:
    if cnt==a-1:
        print(queue.popleft(),end='')
        break
    for i in range(b-1):
        queue.append(queue.popleft())
    print(queue.popleft(),end=', ')
    cnt+=1
print('>')
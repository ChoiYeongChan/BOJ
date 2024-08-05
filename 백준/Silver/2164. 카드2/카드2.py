import sys
from collections import deque
input=sys.stdin.readline
queue=deque([])
n=int(input())
for i in range(n):
    queue.append(i+1)
res=0
while queue:
    res=queue.popleft()
    if queue:
        queue.append(queue.popleft())
    else:
        print(res)
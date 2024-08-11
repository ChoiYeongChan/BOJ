import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
visited=[0]*(100001)
queue=deque([])
queue.append(n)
while queue:
    x=queue.popleft()
    if x==k:
        print(visited[x])
        break
    for nx in (x-1,x+1,x*2):
        if 0<=nx<=100000 and not visited[nx]:
            visited[nx]=visited[x]+1
            queue.append(nx)
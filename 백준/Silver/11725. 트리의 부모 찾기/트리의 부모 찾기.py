import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
graph=[[]for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
queue=deque()
queue.append(1)
ans=[0]*(n+1)
while queue:
    x=queue.popleft()
    for i in graph[x]:
        if ans[i]==0:
            ans[i]=x
            queue.append(i)
for i in range(2,n+1):
    print(ans[i])
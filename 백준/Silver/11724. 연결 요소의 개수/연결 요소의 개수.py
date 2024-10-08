import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[]for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt=0
visited=[False]*(n+1)
def bfs(i):
    queue=deque([])
    queue.append(i)
    visited[i]=True
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        cnt+=1
print(cnt)
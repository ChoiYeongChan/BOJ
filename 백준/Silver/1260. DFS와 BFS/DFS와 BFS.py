import sys
from collections import deque
input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[]for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
def dfs(start):
    visited1[start]=True
    print(start, end=' ')
    for i in graph[start]:
        if not visited1[i]:
            dfs(i)
def bfs(start):
    queue=deque([start])
    visited2[start]=True
    while queue:
        x=queue.popleft()
        print(x,end=" ")
        for i in graph[x]:
            if not visited2[i]:
                visited2[i]=True
                queue.append(i)
visited1=[False]*(n+1)
visited2=[False]*(n+1)
dfs(v)
print()
bfs(v)
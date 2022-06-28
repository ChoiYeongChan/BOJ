import sys
from collections import deque
def bfs(graph,start,visited):
    queue=deque()
    queue.append(start)
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if visited[i]==0:
                visited[i]=visited[v]+1
                queue.append(i)
input=sys.stdin.readline
n=int(input())
graph=[[]for _ in range(n+1)]
a,b=map(int,input().split())
m=int(input())
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited=[0]*(n+1)
bfs(graph,a,visited)
if visited[b]>0:
    print(visited[b])
else:
    print('-1')
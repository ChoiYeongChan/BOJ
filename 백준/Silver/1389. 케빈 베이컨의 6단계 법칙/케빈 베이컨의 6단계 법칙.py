import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
def bfs(start):
    num=[0]*(n+1)
    visited=[False]*(n+1)
    queue=deque([start])
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                num[i]=num[x]+1
                visited[i]=True
                queue.append(i)
    return sum(num)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans=[]
for i in range(1,n+1):
    ans.append(bfs(i))
print(ans.index(min(ans))+1)
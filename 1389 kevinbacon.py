import sys
from collections import deque
def bfs(i):
    visited=[0]*(n+1)
    queue.append(i)
    visited[i]=1
    while queue:
        t=queue.popleft()
        for j in matrix[t]:
            if not visited[j]:
                visited[j]=visited[t]+1
                queue.append(j)
    return sum(visited)
n,m=map(int,sys.stdin.readline().split())
matrix=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    matrix[x].append(y)
    matrix[y].append(x)
queue=deque()
ans=[]
for i in range(1,n+1):
    ans.append(bfs(i))
print(ans.index(min(ans))+1)
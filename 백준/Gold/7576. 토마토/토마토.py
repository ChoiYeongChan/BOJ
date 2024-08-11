import sys
from collections import deque
input=sys.stdin.readline
m,n=map(int,input().split())
graph=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
cnt=0
queue=deque([])
for _ in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append((i,j))
while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            graph[nx][ny]=graph[x][y]+1
            queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            print(-1)
            exit(0)
        else:
            cnt=max(cnt,graph[i][j])
print(cnt-1)
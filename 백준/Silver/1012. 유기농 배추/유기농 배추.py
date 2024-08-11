import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    graph[i][j]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=0
for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    cnt=0
    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)
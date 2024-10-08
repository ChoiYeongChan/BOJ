import sys
from collections import deque
import copy
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs():
    queue=deque()
    tmp=copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                queue.append((i,j))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny]==0:
                tmp[nx][ny]=2
                queue.append((nx,ny))
    global ans
    cnt=0
    for i in range(n):
        cnt+=tmp[i].count(0)
    ans=max(ans,cnt)
def wall(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                wall(cnt+1)
                graph[i][j]=0
for _ in range(n):
    graph.append(list(map(int,input().split())))
ans=0
wall(0)
print(ans)
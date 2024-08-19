import sys
from collections import deque
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[-1,1,0,0]
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(input().rstrip()))

visited=[[False]*n for _ in range(n)]
cnt1=0

def bfs(a,b):
    queue=deque()
    queue.append((a,b))
    visited[a][b]=True
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny))

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1+=1

for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'
visited=[[False]*n for _ in range(n)]
cnt2=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2+=1
print(cnt1,cnt2)
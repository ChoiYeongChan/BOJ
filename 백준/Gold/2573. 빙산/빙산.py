import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
year=0
def bfs(a,b):
    queue=deque()
    queue.append([a,b])
    visited[a][b]=True
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny]:
                    visited[nx][ny]=True
                    queue.append([nx,ny])
                else:
                    cnt[x][y]+=1
    return 1
while True:
    visited=[[0]*m for _ in range(n)]
    answer=[]
    cnt=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                answer.append(bfs(i,j))
    for i in range(n):
        for j in range(m):
            graph[i][j]-=cnt[i][j]
            if graph[i][j]<0:
                graph[i][j]=0
    if len(answer)==0 or len(answer)>=2:
        break
    year+=1
if len(answer)>=2:
    print(year)
else:
    print(0)
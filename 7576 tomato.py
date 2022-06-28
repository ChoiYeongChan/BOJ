import sys
from collections import deque
m,n=map(int,sys.stdin.readline().split())
tomato=[]
queue=deque()
dx,dy=[-1,1,0,0],[0,0,-1,1]
ans=0
for i in range(n):
    tomato.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if tomato[i][j]==1:
            queue.append([i,j])

def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<m and tomato[nx][ny]==0:
                tomato[nx][ny]=tomato[x][y]+1
                queue.append([nx,ny])
bfs()
for i in tomato:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    ans=max(ans,max(i))
print(ans-1)
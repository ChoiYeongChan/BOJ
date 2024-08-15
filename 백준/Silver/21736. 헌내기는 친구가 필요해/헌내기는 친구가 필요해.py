import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
queue=deque([])
start=[]
for i in range(n):
    row=list(input().rstrip())
    for j in range(m):
        if row[j]=='I':
            start.append([i,j])
            queue.append([i,j])
    graph.append(row)
visited=[[False]*m for _ in range(n)]
cnt=0
visited[start[0][0]][start[0][1]]=True
while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]!='X' and not visited[nx][ny]:
                queue.append([nx,ny])
                visited[nx][ny]=True
                if graph[nx][ny]=='P':
                    cnt+=1
if cnt==0:
    print('TT')
else:
    print(cnt)
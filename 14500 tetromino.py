import sys
n,m=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
visited=[[False]*m for _ in range(n)]
max_val=max(map(max,graph))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
ans = 0

def dfs(x,y,idx,total):
    global ans
    if ans>=total + max_val*(3-idx):
        return
    if idx==3:
        ans=max(ans,total)
        return
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                if idx==1:
                    visited[nx][ny]=1
                    dfs(x,y,idx+1,total+graph[nx][ny])
                    visited[nx][ny]=0
                visited[nx][ny]=1
                dfs(nx,ny,idx+1,total+graph[nx][ny])
                visited[nx][ny]=0

for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i,j,0,graph[i][j])
        visited[i][j]=0
print(ans)

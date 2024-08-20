import sys
input=sys.stdin.readline
def dfs(x,y,cnt,total):
    global ans
    if ans>=total+max_val*(3-cnt):
        return # 어차피 작으면 중단
    if cnt==3:
        ans=max(ans,total)
        return
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if cnt==1: # ㅗ 모양
                    visited[nx][ny]=True
                    dfs(x,y,cnt+1,total+graph[nx][ny])
                    visited[nx][ny]=False
                visited[nx][ny]=True
                dfs(nx,ny,cnt+1,total+graph[nx][ny])
                visited[nx][ny]=False
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
visited=[[False]*m for _ in range(n)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
ans=0
max_val=max(map(max,graph))
for x in range(n):
    for y in range(m):
        visited[x][y]=1
        dfs(x,y,0,graph[x][y])
        visited[x][y]=0
print(ans)
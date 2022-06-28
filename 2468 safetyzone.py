import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,h):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if (0<=nx<n) and (0<=ny<n):
            if graph[nx][ny]>h and not visited[nx][ny]:
                visited[nx][ny]=True
                dfs(nx,ny,h)

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

ans=0

for k in range(max(map(max,graph))):
    cnt=0
    visited=[[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j]>k and not visited[i][j]:
                visited[i][j]=True
                cnt+=1
                dfs(i,j,k)
    ans=max(ans,cnt)

print(ans)
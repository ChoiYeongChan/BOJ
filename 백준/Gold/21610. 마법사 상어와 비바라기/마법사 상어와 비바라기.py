import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
moves=[list(map(int,input().split())) for _ in range(m)]
dx8=[0,-1,-1,0,1,1,1,0,-1]
dy8=[0,0,-1,-1,-1,0,1,1,1]
dx4=[-1,1,-1,1]
dy4=[-1,-1,1,1]
clouds=[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
for d,s in moves:
    moved=[]
    for y,x in clouds:
        nx=(x+dx8[d]*s)%n
        ny=(y+dy8[d]*s)%n
        graph[ny][nx]+=1
        moved.append((ny,nx))
    for y,x in moved:
        cnt=0
        for i in range(4):
            nx=x+dx4[i]
            ny=y+dy4[i]
            if ny<0 or nx<0 or ny>=n or nx>=n:
                continue
            elif graph[ny][nx]>0:
                cnt+=1
        graph[y][x]+=cnt
    new=[]
    for y in range(n):
        for x in range(n):
            if (y,x) in moved or graph[y][x]<2:
                continue
            graph[y][x]-=2
            new.append((y,x))
    clouds=new
ans=0
for y in range(n):
    for x in range(n):
        ans+=graph[y][x]
print(ans)
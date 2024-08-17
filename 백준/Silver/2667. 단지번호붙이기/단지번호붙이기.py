import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
dx=[1,-1,0,0]
dy=[0,0,-1,1]
graph=[]
def bfs(a,b):
    queue=deque([(a,b)])
    graph[a][b]=0
    count=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                graph[nx][ny]=0
                count+=1
                queue.append((nx,ny))
    return count
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))
cnt=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt.append(bfs(i,j))
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)
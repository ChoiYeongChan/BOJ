import sys
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
n=int(sys.stdin.readline())
matrix=[[] for _ in range(n)]
for i in range(n):
    matrix[i]=list(map(int,sys.stdin.readline().rstrip()))
cnt=[]
def bfs(a,b):
    n=len(matrix)
    queue=deque()
    queue.append((a,b))
    matrix[a][b]=0
    count=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if matrix[nx][ny]==1:
                matrix[nx][ny]=0
                queue.append((nx,ny))
                count+=1
    return count
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            cnt.append(bfs(i,j))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)
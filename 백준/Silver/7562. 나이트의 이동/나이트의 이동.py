import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
def bfs(x1,y1,x2,y2):
    q=deque()
    q.append([x1,y1])
    board[x1][y1]=1
    while q:
        x,y=q.popleft()
        if x==x2 and y==y2:
            return board[x][y]-1
        else:
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<l and 0<=ny<l:
                    if board[nx][ny]==0:
                        q.append([nx,ny])
                        board[nx][ny]=board[x][y]+1
for _ in range(n):
    l=int(input())
    board=[[0 for _ in range(l)] for _ in range(l)]
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    if x1==x2 and y1==y2:
        print(0)
    else:
        ans=bfs(x1,y1,x2,y2)
        print(ans)
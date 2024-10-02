from collections import deque
def solution(land):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    n=len(land)
    m=len(land[0])
    result=[0 for _ in range(m+1)]
    visited=[[0 for _ in range(m)] for _ in range(n)]
    answer = 0
    def bfs(a,b):
        cnt=0
        q=deque()
        q.append((a,b))
        visited[a][b]=1
        miny,maxy=b,b
        while q:
            cnt+=1
            x,y=q.popleft()
            miny=min(miny,y)
            maxy=max(maxy,y)
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if visited[nx][ny]==0 and land[nx][ny]==1:
                        visited[nx][ny]=1
                        q.append((nx,ny))
        for i in range(miny,maxy+1):
            result[i]+=cnt
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0 and land[i][j]==1:
                bfs(i,j)
    answer=max(result)
    return answer
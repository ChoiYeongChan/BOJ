from collections import deque
T=int(input())
way = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 좌, 상, 우, 하
pipe = [[], [0, 1, 2, 3], [1, 3], [0, 2], [1, 2], [3, 2], [3, 0], [1, 0]]
for test_case in range(1,T+1):
    N,M,R,C,L=map(int,input().split())
    graph=[]
    cnt=0
    visited=[[0]*M for _ in range(N)]
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    q=deque()
    q.append((R,C))
    visited[R][C]=1
    while q:
        x,y=q.popleft()
        sub=pipe[graph[x][y]]
        if sub==[]:
            continue
        for i in sub:
            dx,dy=way[i]
            nx=x+dx
            ny=y+dy
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and graph[nx][ny]!=0:
                next=pipe[graph[nx][ny]]
                for j in next:
                    mx=nx+way[j][0]
                    my=ny+way[j][1]
                    if mx==x and my==y:
                        q.append((nx,ny))
                        visited[nx][ny]=visited[x][y]+1
                
    for i in range(N):
        for j in range(M):
            if 0<visited[i][j]<=L:
                cnt += 1
    print('#'+str(test_case),cnt)
import sys
input=sys.stdin.readline
m,n,k=map(int,input().split())
dx=[0,0,-1,1]
dy=[-1,1,0,0]
cnt=[]
g=[[0]*n for _ in range(m)]
for _ in range(k):
    a,b,c,d=map(int,input().split())
    for j in range(a,c):
        for i in range(b,d):
            g[i][j]=1
for i in range(m):
    for j in range(n):
        if g[i][j]==0:
            count=1
            g[i][j]=1
            queue=[[i,j]]
            while queue:
                x,y=queue[0][0],queue[0][1]
                del queue[0]
                for k in range(4):
                    x1=x+dx[k]
                    y1=y+dy[k]
                    if 0<=x1<m and 0<=y1<n and g[x1][y1]==0:
                        g[x1][y1]=1
                        count+=1
                        queue.append([x1,y1])
            cnt.append(count)
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i,end=' ')
import sys
input=sys.stdin.readline
INF=sys.maxsize
n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=min(c,graph[a][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print("0", end=" ")
        else:
            print(graph[i][j],end=" ")
    print()
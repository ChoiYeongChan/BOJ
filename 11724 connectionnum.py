import sys
sys.setrecursionlimit(10000)
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
graph[0]=[0,0]
visited=[False for _ in range(n+1)]
def dfs(start,visited):
    visited[start]=True
    for i in graph[start]:
        if visited[i]==False:
            dfs(i,visited)
for _ in range(m):
    start,end=map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
cnt=0
for i in range(1,n+1):
    if visited[i]==False:
        cnt+=1
        dfs(i,visited)
print(cnt)
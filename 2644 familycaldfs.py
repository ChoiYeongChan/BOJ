import sys
def dfs(graph,v,visited):
    for i in graph[v]:
        if visited[i]==0:
            visited[i]=visited[v]+1
            dfs(graph,i,visited)
input=sys.stdin.readline
n=int(input())
graph=[[]for _ in range(n+1)]
a,b=map(int,input().split())
m=int(input())
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited=[0]*(n+1)
dfs(graph,a,visited)
if visited[b]>0:
    print(visited[b])
else:
    print('-1')
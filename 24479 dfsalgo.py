import sys

n, m, r = map(int, sys.stdin.readline().split())

nodes = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
nodes_cnt = [0 for _ in range(n+1)]
for _ in range(m):
    tail, head = map(int, sys.stdin.readline().rstrip().split())
    nodes[tail].append(head)
    nodes[head].append(tail)

for i in range(n+1):
    nodes[i].sort(reverse=True)
cnt = 1

stack = []
stack.append(r)

while stack:
    cur_node = stack.pop()
    visited[cur_node] = True
    if nodes_cnt[cur_node] == 0:
        nodes_cnt[cur_node] = cnt
        cnt += 1

    for next_node in nodes[cur_node]:
        if not visited[next_node]:
            stack.append(next_node)

for cnt in nodes_cnt[1:]:
    print(cnt)

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)
node=[0]*(n+1)
for i in range(n+1):
    graph[i].sort()
cnt=1
def dfs(v):
    global cnt
    visited[v]=True
    if node[v]==0:
        node[v]=cnt
        cnt+=1
    for i in graph[v]:        
        if not visited[i]:
            dfs(i)
dfs(1)
for i in range(1,n+1):
    print(node[i])
import sys
import heapq
input=sys.stdin.readline
INF=sys.maxsize
V,E=map(int,input().split())
k=int(input())
dp=[INF]*(V+1)
heap=[]
graph=[[]for _ in range(V+1)]

for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))
dp[k]=0
heapq.heappush(heap,(0,k))
while heap:
    weight,now=heapq.heappop(heap)
    if dp[now]<weight:
        continue
    for w,next in graph[now]:
        next_weight=w+weight
        if next_weight<dp[next]:
            dp[next]=next_weight
            heapq.heappush(heap,(next_weight,next))
for i in range(1,V+1):
    if dp[i]==INF:
        print("INF")
    else:
        print(dp[i])
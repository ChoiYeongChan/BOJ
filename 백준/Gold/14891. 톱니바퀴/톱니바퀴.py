import sys
from collections import deque
input=sys.stdin.readline
graph=[deque(list(map(int,input().rstrip()))) for _ in range(4)]
k=int(input())
def right(idx,d):
    if idx>3:
        return
    if graph[idx-1][2]!=graph[idx][6]:
        right(idx+1,-d)
        graph[idx].rotate(d)
def left(idx,d):
    if idx<0:
        return
    if graph[idx][2]!=graph[idx+1][6]:
        left(idx-1,-d)
        graph[idx].rotate(d)
for _ in range(k):
    i,d=map(int,input().split())
    i-=1
    left(i-1,-d)
    right(i+1,-d)
    graph[i].rotate(d)
ans=0
for i in range(4):
    if graph[i][0]==1:
        ans+=2**i
print(ans)
import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
ladders={}
for _ in range(n):
    x,y=map(int,input().split())
    ladders[x]=y
snakes={}
for _ in range(m):
    x,y=map(int,input().split())
    snakes[x]=y
queue=deque()
visited=[0]*101
queue.append(1)
cnt=0
flag=True
while flag:
    for _ in range(len(queue)):
        x=queue.popleft()
        if x==100:
            print(cnt)
            flag=False
            break
        for i in range(1,7):
            nx=x+i
            if nx<=100 and visited[nx]==0:
                visited[nx]=1
                if nx in ladders.keys():
                    visited[ladders[nx]]=1
                    queue.append(ladders[nx])
                elif nx in snakes.keys():
                    visited[snakes[nx]]=1
                    queue.append(snakes[nx])
                else:
                    queue.append(nx)
    cnt+=1
import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
t=[0]*100001
def bfs(x,y):
    queue=deque()
    if x==0:
        queue.append(1)
    else:
        queue.append(x)
    while queue:
        x=queue.popleft()
        if x==y:
            return t[x]
        for nx in (x-1,x+1,x*2):
            if 0<=nx<100001 and t[nx]==0:
                if nx==2*x:
                    t[nx]=t[x]
                    queue.appendleft(nx)
                else:
                    t[nx]=t[x]+1
                    queue.append(nx)
if n==0:
    if k==0:
        print(0)
    else:
        print(bfs(n,k)+1)
else:
    print(bfs(n,k))
import sys
input=sys.stdin.readline
n,w,l=map(int,input().split())
queue=list(map(int,input().split()))
b=[0]*w
t=0
while b:
    t+=1
    b.pop(0)
    if queue:
        if sum(b)+queue[0]<=l:
            b.append(queue.pop(0))
        else:
            b.append(0)
print(t)
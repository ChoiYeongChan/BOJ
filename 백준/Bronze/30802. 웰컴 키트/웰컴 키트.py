import sys
input=sys.stdin.readline
n=int(input())
shirt=list(map(int,input().split()))
t,p=map(int,input().split())
tnum=0
pnum=0
pelse=0
for i in shirt:
    if i%t==0:
        tnum+=i//t
    else:
        tnum+=i//t+1
print(tnum)
pnum=n//p
pelse=n%p
print(pnum,pelse)
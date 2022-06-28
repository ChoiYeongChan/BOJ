import sys
n,m=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
x=[0]*(n+1)
x[0]=0
for i in range(0,n):
    x[i+1]=x[i]+a[i]
for _ in range(m):
    i,j=map(int,sys.stdin.readline().split())
    print(x[j]-x[i-1])
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
sum_l=[0]*(n+1)
for i in range(1,n+1):
    sum_l[i]=sum_l[i-1]+l[i-1]
for _ in range(m):
    i,j=map(int,input().split())
    print(sum_l[j]-sum_l[i-1])
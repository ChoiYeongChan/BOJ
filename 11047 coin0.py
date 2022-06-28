import sys
n,k=map(int,sys.stdin.readline().split())
coin=[0]*10
for i in range(n):
    coin[i]=int(sys.stdin.readline())
m=n-1
for i in range(n):
    if coin[i]>k:
        m=i-1
        break
cnt=0
while 1:
    if k%coin[m]==0:
        cnt+=k//coin[m]
        break
    else:
        cnt+=k//coin[m]
        k-=(k//coin[m])*coin[m]
        m-=1
print(cnt)
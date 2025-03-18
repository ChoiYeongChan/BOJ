import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
a.sort()
k=int(input())
x=0
y=n-1
cnt=0
while x<y:
    s=a[x]+a[y]
    if s==k:
        cnt+=1
        x+=1
    elif s<k:
        x+=1
    else:
        y-=1
print(cnt)
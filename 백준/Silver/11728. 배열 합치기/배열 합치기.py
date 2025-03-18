import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
arr=[]
x=0
y=0
while 1:
    if x==n:
        r=b[y:]
        for i in r:
            arr.append(i)
        break
    elif y==m:
        r=a[x:]
        for i in r:
            arr.append(i)
        break
    elif a[x]<=b[y]:
        arr.append(a[x])
        x+=1
    elif a[x]>b[y]:
        arr.append(b[y])
        y+=1

print(*arr, sep=' ')
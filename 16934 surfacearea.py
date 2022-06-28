import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
up=n*m
left=0
for i in range(n):
    for j in range(m):
        if j==0:
            left+=a[i][j]
        else:
            if a[i][j]>a[i][j-1]:
                left+=a[i][j]-a[i][j-1]
front=0
for j in range(m):
    for i in range(n):
        if i==0:
            front+=a[i][j]
        else:
            if a[i][j]>a[i-1][j]:
                front+=a[i][j]-a[i-1][j]
s=2*(up+left+front)
print(s)    